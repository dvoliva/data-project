from fastapi import FastAPI
from src.config import API_TITLE, API_VERSION, API_DESCRIPTION

from src.routers import sales
from src.routers import reviews

app = FastAPI(
    title=API_TITLE,
    version=API_VERSION,
    description=API_DESCRIPTION
)

app.include_router(sales.router)
app.include_router(reviews.router)

@app.get("/", tags=["Health"])
async def root():
    return {
        "message": "Bienvenido a la Mock API",
        "status": "active",
        "version": API_VERSION
    }