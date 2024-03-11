from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .models import Product
from .schemas import ProductEdit

router = APIRouter()

@router.put("/products/{product_id}", response_model=Product)
def edit_product(product_id: int, product: ProductEdit, db: Session = Depends(get_db)):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    # Update the product with the new information
    db_product.name = product.name
    db_product.price = product.price
    db.commit()
    return db_product
