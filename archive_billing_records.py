provider "azurerm" {
  features {}
}

resource "azurerm_cosmosdb_account" "example" {
  name                = "example-cosmosdb-account"
  location            = "West US"
  resource_group_name = "example-resources"
  offer_type          = "Standard"
  kind                = "GlobalDocumentDB"
  consistency_policy {
    consistency_level = "Session"
  }
}

resource "azurerm_cosmosdb_sql_database" "example" {
  name                = "example-cosmosdb-database"
  resource_group_name = "example-resources"
  account_name        = azurerm_cosmosdb_account.example.name
}

resource "azurerm_cosmosdb_sql_container" "example" {
  name                = "example-cosmosdb-container"
  resource_group_name = "example-resources"
  account_name        = azurerm_cosmosdb_account.example.name
  database_name       = azurerm_cosmosdb_sql_database.example.name
  partition_key_path  = "/partitionKey"
}

resource "azurerm_storage_account" "example" {
  name                     = "examplestorageacct"
  resource_group_name      = "example-resources"
  location                 = "West US"
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

resource "azurerm_storage_container" "example" {
  name                  = "archived-billing-records"
  storage_account_name  = azurerm_storage_account.example.name
  container_access_type = "private"
}
