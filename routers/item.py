from fastapi import APIRouter
from typing import Optional
from pydantic import BaseModel

router = APIRouter()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


@router.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@router.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"id": item_id, "name": item.name, "item_price": item.price}
