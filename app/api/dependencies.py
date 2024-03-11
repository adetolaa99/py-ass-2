from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from .models import User

def check_unique_username(username: str, db: Session):
    user = db.query(User).filter(User.username == username).first()
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists",
        )
    return username
