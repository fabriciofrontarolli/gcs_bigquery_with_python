from google.cloud import storage
from google.cloud import bigquery

# Initialize Clients
storage_client = storage.Client()
bigquery_client = bigquery.Client()

def explicit():
    from google.coud import storage


def fetchInvoiceDataFromBucket(fileName):
    # The bucket should already exists in the project
    bucket_name = "fabriciofrontarolli"
    bucket = storage_client.get_bucket(bucket_name)
    invoiceFile = bucket.get_blob("invoice.csv")
    return invoiceFile


def loadInvoiceToBigQuery(file):
    # The Dataset should already exists in the project
    dataset_name = "fabriciofrontarolli"
    table_name = "invoice"
    dataset_ref = bigquery_client.dataset(dataset_name)
    table_ref = dataset_ref.table(table_name)
    job_config = bigquery.LoadJobConfig()
    job_config.source_format = bigquery.SourceFormat.CSV
    job_config.skip_leading_rows = 1
    job_config.autodetect = True
    with open(filename, 'rb') as source_file:
    job = client.load_table_from_file(
        source_file,
        table_ref,
        location='US',  # Must match the destination dataset location.
        job_config=job_config)  # API request

    job.result()  # Waits for table load to complete.

    print('Loaded {} rows into {}:{}.'.format(
        job.output_rows, dataset_id, table_id))
