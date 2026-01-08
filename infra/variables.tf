variable "project_id" {
    description = "gcp project id where resources will be created"
    type        = string 
}

variable "region" {
    description = "default gcp region where resources will be created"
    type        = string
    default     = "us-central1"
}
