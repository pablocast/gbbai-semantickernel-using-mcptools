Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

$envFilePath = ".env"

If (Test-Path $envFilePath) {
    Remove-Item $envFilePath -Force
}
New-Item -Path $envFilePath -ItemType File -Force | Out-Null

Add-Content -Path $envFilePath -Value ("APIM_RESOURCE_GATEWAY_URL=" + (azd env get-value PROJECT_CONNECTION_STRING))
Add-Content -Path $envFilePath -Value ("APIM_SUBSCRIPTION_KEY=" + (azd env get-value AZURE_SEARCH_ENDPOINT))
Add-Content -Path $envFilePath -Value ("AZURE_OPENAI_API_VERSION=" + (azd env get-value AZURE_STORAGE_CONNECTION_STRING))
Add-Content -Path $envFilePath -Value ("AZURE_OPENAI_DEPLOYMENT_NAME=" + (azd env get-value AZURE_OPENAI_ENDPOINT))

