from fastapi import APIRouter, Query
from typing import List

from src.domain.models import SalesTransaction
from src.domain.generator import SalesGenerator

router = APIRouter()

sales_generator = SalesGenerator()

@router.get("/sales/", response_model=List[SalesTransaction])
def get_sales(
    count: int = Query(10, ge=1, le=1000, description="Número de transacciones de ventas a generar")
):
    print(f"generando {count} transacciones de ventas simuladas.")
    data = sales_generator.generate_sales(count)
    return data

