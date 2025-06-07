from sqlalchemy.orm import Session
from . import models, schemas
from fastapi import HTTPException
from datetime import datetime

def get_classes(db: Session):
    """Retrieve all upcoming fitness classes."""
    return db.query(models.FitnessClass).filter(models.FitnessClass.datetime >= datetime.now()).all()

def create_booking(db: Session, booking: schemas.BookingIn):
    """Create a booking for a specific class."""
    fitness_class = db.query(models.FitnessClass).filter(models.FitnessClass.id == booking.class_id).first()

    if not fitness_class:
        raise HTTPException(status_code=404, detail="Class not found")
    
    if fitness_class.available_slots < 1:
        raise HTTPException(status_code=400, detail="No available slots")

    db_booking = models.Booking(**booking.dict())
    fitness_class.available_slots -= 1
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking

def get_bookings_by_email(db: Session, email: str):
    """Get all bookings for a given client email."""
    return db.query(models.Booking).filter(models.Booking.client_email == email).all()
