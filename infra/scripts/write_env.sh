#!/bin/sh

envFilePath=".env"

# Remove the file if it exists
[ -f "$envFilePath" ] && rm -f "$envFilePath"

# Create a new empty file
touch "$envFilePath"

# Append environment variable values to the file
echo "APIM_RESOURCE_GATEWAY_URL=$(azd env get-value apimResourceGatewayUR)" >> "$envFilePath"
echo "APIM_SUBSCRIPTION_KEY=$(azd env get-value apimSubscriptionKey)" >> "$envFilePath"
echo "AZURE_OPENAI_API_VERSION=$(azd env get-value openAIAPIVersion)" >> "$envFilePath"
echo "AZURE_OPENAI_DEPLOYMENT_NAME=$(azd env get-value openAIModelName)" >> "$envFilePath"
