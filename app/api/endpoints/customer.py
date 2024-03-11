from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .models import Customer
from .schemas import CustomerEdit
from .dependencies import check_unique_username

router = APIRouter()

@router.put("/customers/{customer_id}", response_model=Customer)
def edit_customer(customer_id: int, customer: CustomerEdit, db: Session = Depends(get_db)):
    db_customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if not db_customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    # Update the customer with the new information
    db_customer.username = customer.username
    db_customer.email = customer.email
    db.commit()
    return db_customer
