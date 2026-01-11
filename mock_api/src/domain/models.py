from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class Review(BaseModel):
    review_id: int 
    product_id: int 
    user_id: int 
    rating: int  
    review_date: str
    review_text: str
    summary: Optional[str] = None

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
