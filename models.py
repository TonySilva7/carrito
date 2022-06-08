from pydantic import BaseModel, Field, constr, confloat

validate_str = constr(min_length=3, max_length=50, strict=True)
validate_float = confloat(gt=0.0, strict=True)


class BaseProduct(BaseModel):
    name: validate_str = Field(...)
    brand: validate_str = Field(...)
    price: validate_float = Field(...)  # greater than 0.0


class Product(BaseProduct):
    id: int = Field(...)
