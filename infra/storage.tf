resource "google_storage_bucket" "data_lake" {
    name = "data_lake-${var.project_id}"
    location = var.region
    storage_class = "STANDARD"

    uniform_bucket_level_access = true

    versioning{
        enabled = true
    }

    force_destroy = true
}

resource "google_storage_bucket" "tf_state" {
    name = "tf-state-${var.project_id}"
    location = var.region
    storage_class = "STANDARD"

    uniform_bucket_level_access = true

    versioning{
        enabled = true
    }

    force_destroy = false
}