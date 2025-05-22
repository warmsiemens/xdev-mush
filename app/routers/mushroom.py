from fastapi import APIRouter, HTTPException
from app.schemas.mushroom import MushroomCreate, MushroomUpdate
from app.models.mushroom import Mushroom
from app.services import mushroom_service

router = APIRouter()


@router.post("/", response_model=Mushroom)
def create(mushroom: MushroomCreate):
    return mushroom_service.create_mushroom(mushroom)


@router.put("/{mushroom_id}", response_model=Mushroom)
def update(mushroom_id: str, mushroom: MushroomUpdate):
    try:
        return mushroom_service.update_mushroom(mushroom_id, mushroom)
    except KeyError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/{mushroom_id}", response_model=Mushroom)
def get(mushroom_id: str):
    try:
        return mushroom_service.get_mushroom(mushroom_id)
    except KeyError as e:
        raise HTTPException(status_code=404, detail=str(e))
