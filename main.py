from fastapi import FastAPI, Body, status, Query
from models import BaseProduct
from db import Cart
from typing import Optional

app = FastAPI()

cart = Cart()


@app.post("/cart/add_product", status_code=status.HTTP_201_CREATED)
async def add_product(product: BaseProduct = Body(...)):
    cart.add_product(product)
    return {"message": "Product added to cart"}


@app.get("/cart/get_products", status_code=status.HTTP_200_OK)
async def get_products(id: Optional[int] = Query(default=None)):
    if id:
        return cart.get_products(id)
    return cart.get_products()
