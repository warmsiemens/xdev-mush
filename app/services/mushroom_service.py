from uuid import uuid4
from app.schemas.mushroom import MushroomCreate, MushroomUpdate
from app.models.mushroom import Mushroom
from app.data.information import mushrooms_storage


def create_mushroom(mushroom: MushroomCreate) -> Mushroom:
    mushroom_id = str(uuid4())
    new_mushroom = Mushroom(id=mushroom_id, **mushroom.dict())
    mushrooms_storage[mushroom_id] = new_mushroom
    return new_mushroom  # можем так делать, потому что в нашем случае модели тоже pydantic


def update_mushroom(mushroom_id: str, mushroom: MushroomUpdate) -> Mushroom:
    if mushroom_id not in mushrooms_storage:
        raise KeyError('Mushroom not found')

    existing_mushroom = mushrooms_storage[mushroom_id].dict()
    new_information = mushroom.dict(exclude_unset=True)
    existing_mushroom.update(new_information)
    updated = Mushroom(**existing_mushroom)
    mushrooms_storage[mushroom_id] = updated

    return updated


def get_mushroom(mushroom_id: str) -> Mushroom:
    if mushroom_id not in mushrooms_storage:
        raise KeyError('Mushroom not found')

    return mushrooms_storage[mushroom_id]
