from pydantic import BaseModel, Field, constr, confloat, create_model
from typing import Optional

validate_str = constr(
    max_length=50,
    min_length=3,
    strict=True
)

validate_float = confloat(
    gt=0.0,
    strict=True
)


class BaseProducto(BaseModel):
    nombre: validate_str = Field(...)
    marca: validate_str = Field(...)
    precio: validate_float = Field(...)

    @classmethod
    def as_optional(cls):
        annonations = cls.__fields__
        fields = {attribute: (Optional[data_type.type_], None) for attribute, data_type in annonations.items()}
        OptionalModel = create_model(f"Optional{cls.__name__}", **fields)
        return OptionalModel


class Producto(BaseProducto):
    id: int = Field(...)
