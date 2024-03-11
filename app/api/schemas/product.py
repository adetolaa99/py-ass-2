from pydantic import BaseModel

class ProductEdit(BaseModel):
    name: str
    price: int
