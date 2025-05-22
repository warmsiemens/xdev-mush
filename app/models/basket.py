from pydantic import BaseModel, PositiveFloat
from typing import List


class Basket(BaseModel):
    id: str
    owner: str
    capacity: PositiveFloat
    mushrooms: List[str]
