from fastapi import FastAPI
from app.routers import cards, sets

app = FastAPI(title="Cardly API")

app.include_router(cards.router)
app.include_router(sets.router)
