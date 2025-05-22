from pydantic import BaseModel, PositiveFloat


class Mushroom(BaseModel):
    id: str
    name: str
    edibility: bool
    weight: PositiveFloat
    freshness: bool
