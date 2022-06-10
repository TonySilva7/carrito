from fastapi import FastAPI, Body, status, Query, Response, Path
from models import BaseProducto
from db import Carrito

from typing import Optional

app = FastAPI()
carrito = Carrito()


def producto_no_existe():
    return Response(content="No se encuentra el producto", status_code=status.HTTP_404_NOT_FOUND)


@app.post("/carrito/agregar_producto", status_code=status.HTTP_201_CREATED)
async def agregar_producto(producto: BaseProducto = Body(...)):
    carrito.agregar_producto(producto)
    return {"msg": "Producto agregado al carrito con exito"}


@app.get("/carrito", status_code=status.HTTP_200_OK)
async def mostrar_productos(id: Optional[int] = Query(default=None)):
    if id:
        producto = carrito.obtener_productos(id=id)
        if producto:
            return producto.dict()
        return producto_no_existe()
    return carrito.obtener_productos()


@app.put("/carrito/modificar_producto/{id}", status_code=status.HTTP_200_OK)
async def modificar_producto(id: int = Path(...), nuevos_datos: BaseProducto = Body(...)):
    producto = carrito.obtener_productos(id=id)
    if producto:
        carrito.modificar_producto(producto_viejo=producto, nuevos_datos=nuevos_datos)
        return {"msg": "Producto modificado con exito"}
    return producto_no_existe()


@app.patch("/carrito/modificar_producto/{id}", status_code=status.HTTP_200_OK)
async def modificar_producto(id: int = Path(...), nuevos_datos: BaseProducto.as_optional() = Body(...)):
    producto = carrito.obtener_productos(id=id)
    if producto:
        carrito.modificar_producto(producto_viejo=producto, nuevos_datos=nuevos_datos)
        return {"msg": "Producto modificado con exito"}
    return producto_no_existe()

@app.delete("/carrito/borrar_producto/{id}", status_code=status.HTTP_200_OK)
async def borrar_producto(id: int = Path(...)):
    producto = carrito.obtener_productos(id=id)
    if producto:
        carrito.borrar_producto(producto_a_eliminar=producto)
        return {"msg": "Producto borrado con exito"}
    return producto_no_existe()