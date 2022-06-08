from fastapi import FastAPI, Body
from models import BaseProduct

app = FastAPI()


@app.post("/cart/add_product")
async def add_product(product: BaseProduct = Body(...)):
    return product.dict()
