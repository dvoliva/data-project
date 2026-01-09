resource "google_service_account" "ingestion_sa" {
    account_id = "sa-project-ingestion"
    display_name = "Service Account for Data Ingestion"
    description = "Service Account utilizada por Cloud Functions para la ingesta de datos"
}

resource "google_storage_bucket_iam_member" "ingestion_sa_storage_admin" {
    bucket = google_storage_bucket.data_lake.name
    role   = "roles/storage.objectUser"
    member = "serviceAccount:${google_service_account.ingestion_sa.email}"
}

resource "google_bigquery_dataset_iam_member" "ingestion_sa_bigquery_editor" {
    dataset_id = google_bigquery_dataset.warehouse.dataset_id 
    role = "roles/bigquery.dataEditor"
    member = "serviceAccount:${google_service_account.ingestion_sa.email}"
}
