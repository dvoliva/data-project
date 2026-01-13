import os
from pathlib import Path

# logica de rutas
CURRENT_FILE = Path(__file__).resolve()
SRC_DIR = CURRENT_FILE.parent
PROJECT_ROOT = SRC_DIR.parent
DATA_DIR = PROJECT_ROOT / "data"
REVIEWS_FILE_PATH = PROJECT_ROOT / "src/data/amazon_reviews.json"

# app confg
API_TITLE = "Mock Amazon Reviews API"
API_VERSION = "1.0.0"
API_DESCRIPTION = """
API de simulación para el sistema ERP de ShopifyCL.
Sirve para:
1. Obtener reviews históricas (Real Data).
2. Generar transacciones de ventas sintéticas (Fake Data).
"""
#confg regional faker
FAKER_LOCALE = "es_CL"
