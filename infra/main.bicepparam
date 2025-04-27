using './main.bicep'

param apimSku = 'Basicv2'
param openAIConfig = [{name: 'openai1', location: 'eastus2'}]
param openAIDeploymentName = 'gpt-4.1'
param openAIModelName = 'gpt-4.1'
param openAIModelVersion = '2025-04-14'
param openAIModelSKU = 'GlobalStandard'
param openAIAPIVersion = '2024-10-21'
