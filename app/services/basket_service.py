from typing import List
from uuid import uuid4

from app.models.mushroom import Mushroom
from app.schemas.basket import BasketCreate, BasketDetailed
from app.models.basket import Basket
from app.data.information import baskets_storage, mushrooms_storage


def create_basket(basket: BasketCreate) -> Basket:
    basket_id = str(uuid4())
    new_basket = Basket(id=basket_id, mushrooms=[], **basket.dict())
    baskets_storage[basket_id] = new_basket
    return new_basket # можем так делать, потому что в нашем случае модели тоже pydantic


def add_mushroom_to_basket(basket_id: str, mushroom_id: str) -> Basket:
    if basket_id not in baskets_storage:
        raise KeyError("Basket not found")
    if mushroom_id not in mushrooms_storage:
        raise KeyError("Mushroom not found")

    basket = baskets_storage[basket_id]
    mushroom = mushrooms_storage[mushroom_id]

    sum_weight_of_mushrooms = 0
    for mush_id in basket.mushrooms:
        sum_weight_of_mushrooms += mushrooms_storage[mush_id].weight

    if sum_weight_of_mushrooms + mushroom.weight > basket.capacity:
        raise ValueError("The Basket is full")

    basket.mushrooms.append(mushroom_id)
    return basket


def delete_mushroom_from_basket(basket_id: str, mushroom_id: str) -> Basket:
    if basket_id not in baskets_storage:
        raise KeyError("Basket not found")
    if mushroom_id not in baskets_storage[basket_id].mushrooms:
        raise KeyError("Mushroom not found")

    basket = baskets_storage[basket_id]
    basket.mushrooms.remove(mushroom_id)

    return basket


def get_basket(basket_id: str) -> BasketDetailed:
    if basket_id not in baskets_storage:
        raise KeyError("Basket not found")

    basket = baskets_storage[basket_id]

    mushrooms_lst: List[Mushroom] = []
    for mushroom_id in basket.mushrooms:
        mushroom = mushrooms_storage.get(mushroom_id)
        if mushroom:
            mushrooms_lst.append(mushroom)

    return BasketDetailed(**basket.dict(), mushrooms_lst=mushrooms_lst)
