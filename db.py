from typing import List, NoReturn, Optional
from models import Producto, BaseProducto


class Carrito(object):
    productos: List[Producto] = []
    id_maker: int = 1

    def agregar_producto(self, producto: BaseProducto) -> NoReturn:
        nuevo_producto = Producto(id=self.id_maker, **producto.dict())
        self.productos.append(nuevo_producto)
        self.id_maker += 1

    def obtener_productos(self, id: Optional[int] = None):
        if id:
            for producto in self.productos:
                if id == producto.id:
                    return producto
            return None
        return self.productos

    def modificar_producto(self, producto_viejo: Producto, nuevos_datos: BaseProducto):
        posicion = self.productos.index(producto_viejo)
        self.productos[posicion] = producto_viejo.copy(update=nuevos_datos.dict(exclude_unset=True))
        return True

    def borrar_producto(self, producto_a_eliminar: Producto):
        self.productos.remove(producto_a_eliminar)
        return True