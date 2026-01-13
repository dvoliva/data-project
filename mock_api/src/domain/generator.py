import json
import random
from typing import List
from faker import Faker

from src.config import REVIEWS_FILE_PATH, FAKER_LOCALE
from src.domain.models import SalesTransaction

class SalesGenerator:
    """
    clase responsable de generar datos de ventas simuladas pero
    coherentes con los datos reales de reviews.
    """
    def __init__(self):
        
        self.faker = Faker(FAKER_LOCALE)
        self.products_id = self._load_product_ids()
        print(f"productos cargados: {len(self.products_id)}")
    
    def _load_product_ids(self) -> List[str]:
        """
        lee archivo json de reviews y solo extrae IDs
        """
        if not REVIEWS_FILE_PATH.exists():
            raise FileNotFoundError(f"El archivo {REVIEWS_FILE_PATH} no existe.")
    
        with open(REVIEWS_FILE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            unique_ids = list(set(item['product_id'] for item in data))
            return unique_ids
    
    def generate_sales(self, num_sales: int) -> List[SalesTransaction]:
        """
        genera una lista de transacciones de ventas simuladas
        num_sales: cantidad de ventas a generar
        List[SalesTransaction]: objetos validos de ventas por el modelo
        """
        sales_list = []

        for _ in range(num_sales):
            sale = SalesTransaction(
                transaction_id=self.faker.uuid4(),
                date_time=self.faker.date_time_this_year(),
                customer_id=f'CUST-{self.faker.random_int(min=1000, max=9999)}',
                product_id=random.choice(self.product_ids),
                quantity=random.randint(1, 5),
                unit_price=round(random.uniform(10.0, 500.0), 2),
                total_amount=0,
                payment_method=random.choice(["Credit Card", "Debit Card", "PayPal", "Transfer"])
            )
            sale.total_amount = round(sale.quantity * sale.unit_price, 2)
            
            sales_list.append(sale)
            
        return sales_list
