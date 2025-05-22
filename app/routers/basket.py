from fastapi import APIRouter, HTTPException
from app.schemas.basket import BasketCreate, BasketDetailed
from app.models.basket import Basket
from app.services import basket_service

router = APIRouter()


@router.post("/", response_model=Basket)
def create(basket: BasketCreate):
    return basket_service.create_basket(basket)


@router.get("/{basket_id}", response_model=BasketDetailed)
def get(basket_id: str):
    try:
        return basket_service.get_basket(basket_id)
    except KeyError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/{basket_id}/add/{mushroom_id}")
def add(basket_id: str, mushroom_id: str):
    try:
        basket_service.add_mushroom_to_basket(basket_id, mushroom_id)
    except (KeyError, ValueError) as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"detail": "Mushroom added"}


@router.delete("/{basket_id}/remove/{mushroom_id}")
def remove(basket_id: str, mushroom_id: str):
    try:
        basket_service.delete_mushroom_from_basket(basket_id, mushroom_id)
    except KeyError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return {"detail": "Mushroom removed"}
