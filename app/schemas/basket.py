from typing import List

from pydantic import BaseModel, PositiveFloat

from app.models.mushroom import Mushroom


class BasketCreate(BaseModel):
    owner: str
    capacity: PositiveFloat


class BasketDetailed(BaseModel):
    id: str
    owner: str
    capacity: PositiveFloat
    mushrooms_lst: List[Mushroom]
