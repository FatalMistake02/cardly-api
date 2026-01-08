from fastapi import APIRouter, HTTPException
import httpx
from app.config import SUPABASE_URL, SUPABASE_HEADERS
from app.schemas.card import Card
from typing import List

router = APIRouter(prefix="/sets", tags=["Sets"])

@router.get("/", response_model=List[dict])
async def get_all_sets():
    url = f"{SUPABASE_URL}/pokemon_sets"
    async with httpx.AsyncClient() as client:
        r = await client.get(url, headers=SUPABASE_HEADERS)
    return r.json()


@router.get("/{set_id}", response_model=dict)
async def get_set(set_id: str):
    url = f"{SUPABASE_URL}/pokemon_sets?id=eq.{set_id}"
    async with httpx.AsyncClient() as client:
        r = await client.get(url, headers=SUPABASE_HEADERS)
    data = r.json()
    if not data:
        raise HTTPException(status_code=404, detail="Set not found")
    return data[0]
