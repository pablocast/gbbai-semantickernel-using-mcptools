import argparse
import logging
from typing import Annotated, Any, Literal

import anyio
from azure.identity.aio import DefaultAzureCredential
from dotenv import load_dotenv
from semantic_kernel.agents import ChatCompletionAgent, ChatHistoryAgentThread
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.functions import kernel_function

import nest_asyncio
import uvicorn
from mcp.server.sse import SseServerTransport
from starlette.applications import Starlette
from starlette.routing import Mount, Route

import os

logger = logging.getLogger(__name__)

load_dotenv()

apim_resource_gateway_url = os.getenv("APIM_RESOURCE_GATEWAY_URL")
apim_subscription_key = os.getenv("APIM_SUBSCRIPTION_KEY")
openai_api_version = os.getenv("AZURE_OPENAI_API_VERSION")              
openai_deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")


def parse_arguments():
    parser = argparse.ArgumentParser(description="Run the Semantic Kernel MCP server.")
    parser.add_argument(
        "--transport",
        type=str,
        choices=["sse", "stdio"],
        default="stdio",
        help="Transport method to use (default: stdio).",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=None,
        help="Port to use for SSE transport (required if transport is 'sse').",
    )
    return parser.parse_args()


# Define a simple plugin for the sample
class MenuPlugin:
    """A sample Menu Plugin used for the sample."""

    @kernel_function(description="Provides a list of specials from the menu.")
    def get_specials(self) -> Annotated[str, "Returns the specials from the menu."]:
        return """
        Special Soup: Clam Chowder
        Special Salad: Cobb Salad
        Special Drink: Chai Tea
        """

    @kernel_function(description="Provides the price of the requested menu item.")
    def get_item_price(
        self, menu_item: Annotated[str, "The name of the menu item."]
    ) -> Annotated[str, "Returns the price of the menu item."]:
        return "$9.99"


def create_starlette_app(debug: bool = False) -> Starlette:

    agent = ChatCompletionAgent(
        service=AzureChatCompletion(
            endpoint=apim_resource_gateway_url,
            api_key=apim_subscription_key,
            api_version=openai_api_version,                
            deployment_name=openai_deployment_name
        ),
        name="MenuAgent",
        instructions="Answer questions about the menu.",
        plugins=[MenuPlugin()],  # add the sample plugin to the agent
    )
    
    server = agent.as_mcp_server()

    sse = SseServerTransport("/messages/")

    async def handle_sse(request):
        async with sse.connect_sse(request.scope, request.receive, request._send) as (
            read_stream,
            write_stream,
        ):
            await server.run(read_stream, write_stream, server.create_initialization_options())

    return Starlette(
        debug=True,
        routes=[
            Route("/agent/sse", endpoint=handle_sse),
            Mount("/agent/messages/", app=sse.handle_post_message),
        ],
    )
  
starlette_app = create_starlette_app(debug=True)
    
if __name__ == "__main__":
    args = parse_arguments()
    uvicorn.run(starlette_app, args.host, args.port) 