using './main.bicep'

param apimSku = 'Consumption'
param openAIConfig = [{name: 'openai1', location: 'eastus2'}]
param openAIDeploymentName = 'gpt-4.1'
param openAIModelName = 'gpt-4.1'
param openAIModelVersion = '2025-04-14'
param openAIModelSKU = 'GlobalStandard'
param openAIAPIVersion = '2025-03-01-preview'
