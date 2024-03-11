from pydantic import BaseModel

class CustomerEdit(BaseModel):
    username: str
    email: str
