from pydantic import BaseModel, PositiveFloat
from typing import Optional


class MushroomCreate(BaseModel):
    name: str
    edibility: bool
    weight: PositiveFloat
    freshness: bool


class MushroomUpdate(BaseModel):
    name: Optional[str] = None
    edibility: Optional[bool] = None
    weight: Optional[PositiveFloat] = None
    freshness: Optional[bool] = None
