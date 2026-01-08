from fastapi import APIRouter, HTTPException
import httpx
from app.config import SUPABASE_URL, SUPABASE_HEADERS
from app.schemas.card import Card
from typing import List

router = APIRouter(prefix="/cards", tags=["Cards"])

@router.get("/", response_model=List[Card])
async def get_all_cards():
    url = f"{SUPABASE_URL}/cards"
    async with httpx.AsyncClient() as client:
        r = await client.get(url, headers=SUPABASE_HEADERS)
    if r.status_code != 200:
        raise HTTPException(status_code=r.status_code, detail=r.text)
    return r.json()


@router.get("/{card_id}", response_model=Card)
async def get_card(card_id: str):
    url = f"{SUPABASE_URL}/cards?id=eq.{card_id}"
    async with httpx.AsyncClient() as client:
        r = await client.get(url, headers=SUPABASE_HEADERS)
    data = r.json()
    if not data:
        raise HTTPException(status_code=404, detail="Card not found")
    return data[0]


@router.get("/by_set/{set_id}", response_model=List[Card])
async def get_cards_by_set(set_id: str):
    url = f"{SUPABASE_URL}/cards?set_id=eq.{set_id}&order=number.asc"
    async with httpx.AsyncClient() as client:
        r = await client.get(url, headers=SUPABASE_HEADERS)
    return r.json()


@router.get("/search/", response_model=List[Card])
async def search_cards(q: str):
    url = f"{SUPABASE_URL}/cards?name=ilike.*{q}*"
    async with httpx.AsyncClient() as client:
        r = await client.get(url, headers=SUPABASE_HEADERS)
    return r.json()
