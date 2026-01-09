output "ingestion_sa_email" {
    description = "Email de la Service Account de Ingestión (usar para configurar Cloud Functions)"
    value       = google_service_account.ingestion_sa.email
}

output "data_lake_bucket_name" {
    description = "Nombre del bucket creado para el Data Lake"
    value       = google_storage_bucket.data_lake.name
}