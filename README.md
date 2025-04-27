# <img src="./utils/media/azure_logo.png" alt="Azure Foundry" style="width:30px;height:30px;"/> Semantic Kernel Agent Orchestrator using MCP Tools via Azure API Management

 Model Context Protocol with Azure API Management to enable plug & play of
 tools to LLMs

## 🔧 Prerequisites

+ [azd](https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd), used to deploy all Azure resources and assets used in this sample.
+ [PowerShell Core pwsh](https://github.com/PowerShell/powershell/releases) if using Windows
+ [Python 3.11](https://www.python.org/downloads/release/python-3110/)
+  [An Azure Subscription](https://azure.microsoft.com/free/) with Contributor permissions
+  [Sign in to Azure with Azure CLI](https://learn.microsoft.com/cli/azure/authenticate-azure-cli-interactively)
+  [VS Code](https://code.visualstudio.com/) installed with the [Jupyter notebook extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) enabled

## Instructions

1. **Python Environment Setup** <br>
   ```bash
   python3.11 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Create the infrastructure** <br>
This sample uses [`azd`](https://learn.microsoft.com/azure/developer/azure-developer-cli/) and a bicep template to deploy all Azure resources, including Azure AI Search. 

    - Login to your Azure account: `azd auth login`

    - Create an environment: `azd env new`

    - Run `azd up`.

    + Choose your Azure subscription.
    + Enter a region for the resources.

    The deployment creates multiple Azure resources and runs multiple jobs. It takes several minutes to complete. The deployment is complete when you get a command line notification stating "SUCCESS: Your up workflow to provision and deploy to Azure completed."

3. **Running the Notebook with the Orchestrator** <br>
Open the notebook [orchestrator-model-context-protocol](notebooks/) and execute it to see the orchestrator in action.

4. **Delete the Resources** <br>
You can delete the infrastruture created before by using `azd down --purge`
