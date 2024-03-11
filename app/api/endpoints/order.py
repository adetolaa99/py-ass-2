from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .models import Order
from .schemas import Order

router = APIRouter()

@router.put("/orders/{order_id}/checkout", response_model=Order)
def checkout_order(order_id: int, db: Session = Depends(get_db)):
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    if db_order.status != "pending":
        raise HTTPException(status_code=400, detail="Order is not pending")
    db_order.status = "completed"
    db.commit()
    return db_order
