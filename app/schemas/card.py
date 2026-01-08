from pydantic import BaseModel
from typing import List, Optional, Dict

class Card(BaseModel):
    id: str
    name: str
    supertype: Optional[str]
    subtypes: Optional[List[str]]
    hp: Optional[str]
    types: Optional[List[str]]
    rarity: Optional[str]
    set_id: Optional[str]
    set_name: Optional[str]
    set_series: Optional[str]
    set_symbol_url: Optional[str]
    set_logo_url: Optional[str]
    number: Optional[str]
    artist: Optional[str]
    image_small_url: Optional[str]
    image_large_url: Optional[str]
    variants: Optional[Dict[str, bool]]

    class Config:
        orm_mode = True
