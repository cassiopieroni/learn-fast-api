from typing import Optional, List

from fastapi import FastAPI, Response, status
from pydantic import BaseModel


app = FastAPI()


class Produto(BaseModel):
    id: int
    brand: str
    model: str


produtos: List[Produto] = [
    {
        "id": 1,
        "brand": "nike",
        "model": "air force",
    },
    {
        "id": 2,
        "brand": "adidas",
        "model": "regata",
    },
    {
        "id": 3,
        "brand": "rebook",
        "model": "bermuda",
    },
]


@app.get("/produtos", response_model=List[Produto])
def read_item():
    return produtos


@app.get("/produtos/{item_id}", response_model=Produto)
def read_item(item_id: int, response: Response):
    item_id -= 1

    if item_id < 0:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return
        

    return produtos[item_id]
