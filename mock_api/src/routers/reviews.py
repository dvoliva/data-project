import json
import hashlib
from typing import List
from fastapi import APIRouter, Query, HTTPException

from src.config import REVIEWS_FILE_PATH
from src.domain.models import Review

router = APIRouter()

class ReviewsDataSource:
    def __init__(self):
        self.reviews: List[Review] = self._load_reviews()
        print(f"reviews cargadas: {len(self.reviews)}")

    def _generate_review_id(self, reviewer_id: str, asin: str) -> str:
        """
        Crea un ID único y determinista basado en Usuario + Producto.
        Si corremos esto 1000 veces, dará el mismo ID para la misma review.
        """
        # 1. Creamos una 'firma' única combinando los datos
        signature = f"{reviewer_id}-{asin}"
        
        # 2. Convertimos a Hash MD5 (Hexadecimal)
        # Esto genera un string tipo: "a1b2c3d4..."
        return hashlib.md5(signature.encode('utf-8')).hexdigest()

    def _load_reviews(self) -> List[Review]:
        if not REVIEWS_FILE_PATH.exists():
            print(f"El archivo {REVIEWS_FILE_PATH} no existe.")
            return []
    
        reviews = []
        with open(REVIEWS_FILE_PATH, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    raw = json.loads(line)
                    
                    # Extraemos datos clave
                    r_id = raw.get('reviewerID', '')
                    asin = raw.get('asin', '')
                    
                    # Generamos nuestra PK artificial
                    generated_id = self._generate_review_id(r_id, asin)

                    review = Review(
                        review_id=generated_id,  # <--- ASIGNAMOS EL ID GENERADO
                        reviewer_id=r_id,
                        asin=asin,
                        reviewer_name=raw.get('reviewerName', ''),
                        helpful=raw.get('helpful', [0, 0]),
                        review_text=raw.get('reviewText', ''),
                        overall=raw.get('overall', 0.0),
                        summary=raw.get('summary', ''),
                        unix_review_time=raw.get('unixReviewTime', 0),
                        review_time=raw.get('reviewTime', '')
                    )
                    reviews.append(review)
        return reviews
    
    def get_paginated_reviews(self, limit: int, offset: int) -> List[Review]:
        return self.reviews[offset: offset + limit]

reviews_source = ReviewsDataSource()

@router.get("/reviews/", response_model=List[Review])
async def get_reviews(
    limit: int = Query(20, ge=1, le=100, description="cantidad de reviews por pagina"),
    offset: int = Query(0, ge=0, description="desplazamiento para paginación")
):
    results = reviews_source.get_paginated_reviews(limit, offset)
    return results
