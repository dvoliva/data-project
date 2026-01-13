from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List

class Review(BaseModel):
    review_id: str
    reviewer_id: str
    asin: str  # product_id en Amazon
    reviewer_name: Optional[str] = None
    helpful: List[int] = Field(default_factory=lambda: [0, 0])  # [votos útiles, votos totales]
    review_text: str
    overall: float  # rating 1-5
    summary: Optional[str] = None
    unix_review_time: int
    review_time: str

class SalesTransaction(BaseModel):
    transaction_id: str = Field(
        ..., 
        description="Identificador único universal (UUID v4) de la transacción"
    )

    date_time: datetime = Field(
        ..., 
        description="Fecha y hora exacta de la compra (ISO 8601)"
    )

    customer_id: str = Field(
        ..., 
        description="ID interno del cliente que realizó la compra"
    )

    product_id: str = Field(
        ..., 
        description="ASIN del producto. DEBE existir en el catálogo de reviews."
    )

    quantity: int = Field(
        ..., 
        gt=0, 
        description="Cantidad de unidades vendidas"
    )

    unit_price: float = Field(
        ..., 
        gt=0, 
        description="Precio unitario del producto al momento de la venta"
    )

    total_amount: float = Field(
        ..., 
        description="Total calculado de la transacción (quantity * unit_price)"
    )

    payment_method: str = Field(
        ..., 
        description="Método de pago utilizado (Credit Card, Debit, etc.)"
    )
