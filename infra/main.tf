terraform {
    required_version = ">= 1.5.0"

    required_providers {
        google = {
            source  = "hashicorp/google"
            version = ">= 4.0.0"
        }
    }


    backend "gcs" {
        bucket = "tf-state-data-project-1261"
        prefix = "terraform/state"
    }
}

provider "google" {
    project = var.project_id
    region  = var.region
}
