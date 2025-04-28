output "function_app_name" {
  value = azurerm_function_app.example.name
}

output "cosmosdb_endpoint" {
  value = azurerm_cosmosdb_account.example.endpoint
}

output "storage_account_name" {
  value = azurerm_storage_account.example.name
}
