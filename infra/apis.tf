locals {
    services = toset([
    "iam.googleapis.com",                  # gestión de permisos (fundamental)
    "cloudfunctions.googleapis.com",       # motor de funciones
    "run.googleapis.com",                  # backend para funciones gen 2 (¡crítico!)
    "artifactregistry.googleapis.com",     # almacenamiento de contenedores de funciones
    "cloudbuild.googleapis.com",           # constructor de imágenes para las funciones
    "cloudscheduler.googleapis.com",       # orquestador de tareas programadas
    "bigquery.googleapis.com",             # data warehouse
    "aiplatform.googleapis.com",           # inteligencia artificial (gemini)
    "storage.googleapis.com"               # almacenamiento (ya lo usamos, pero aseguramos)        
    ])
}

resource "google_project_service" "apis" {
    for_each = local.services
    project = var.project_id
    service = each.value

    disable_on_destroy = false
}
