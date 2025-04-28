class BillingRecordService:
    def __init__(self, cosmos_client, blob_service_client):
        self.cosmos_client = cosmos_client
        self.blob_service_client = blob_service_client
        self.database = cosmos_client.get_database_client('BillingDB')
        self.container = self.database.get_container_client('BillingRecords')
        self.blob_container_client = blob_service_client.get_container_client('archived-billing-records')

    def get_record(self, record_id):
        try:
            record = self.container.read_item(record_id, partition_key=record_id)
            return record
        except:
            blob_client = self.blob_container_client.get_blob_client(f"{record_id}.json")
            blob_data = blob_client.download_blob().readall()
            return json.loads(blob_data)

# Usage
billing_service = BillingRecordService(cosmos_client, blob_service_client)
record = billing_service.get_record('random-record-id')
