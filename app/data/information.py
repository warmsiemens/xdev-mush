from typing import Dict
from app.models.mushroom import Mushroom
from app.models.basket import Basket

mushrooms_storage: Dict[str, Mushroom] = {}
baskets_storage: Dict[str, Basket] = {}
