from typing import List, NoReturn, Optional
from models import BaseProduct, Product


class Cart(object):
    products: List[Product] = []
    id_maker: int = 1

    def add_product(self, product: BaseProduct) -> NoReturn:
        new_product: Product = Product(id=self.id_maker, **product.dict())
        self.products.append(new_product)
        self.id_maker += 1

    def get_products(self, id: Optional[int] = None) -> List[Product]:
        if id is None:
            return self.products
        else:
            return [product for product in self.products if product.id == id]
