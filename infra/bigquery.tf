
#creación del dataset
resource "google_bigquery_dataset" "warehouse" {
    dataset_id = "data_warehouse"
    description = "data warehouse para análisis y reportes"
    location = var.region

    default_table_expiration_ms = null

    labels = {
        env = "dev"
        project = "data-project"
    }
}

#creación de tabla raw_sales
resource "google_bigquery_table" "raw_sales" {
    dataset_id = google_bigquery_dataset.warehouse.dataset_id
    table_id = "raw_sales"

    schema = file("${path.module}/schemas/raw_sales.json")

    deletion_protection = false
}

#creación de tabla raw_reviews
resource "google_bigquery_table" "raw_reviews" {
    dataset_id = google_bigquery_dataset.warehouse.dataset_id
    table_id = "raw_reviews"

    schema = file("${path.module}/schemas/raw_reviews.json")

    deletion_protection = false
}