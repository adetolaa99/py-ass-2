from pydantic import BaseModel

class Order(BaseModel):
    id: int
    status: str
