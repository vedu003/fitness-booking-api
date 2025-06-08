"""
Script to initialize the database with sample data.
"""

from .database import SessionLocal, engine
from . import models
from datetime import datetime, timedelta

def seed():
    models.Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    if db.query(models.FitnessClass).first():
        return  # Already seeded

    # Seed sample classes
    classes = [
        models.FitnessClass(name="Yoga", datetime=datetime.now() + timedelta(days=1), instructor="Alice", available_slots=4),
        models.FitnessClass(name="Zumba", datetime=datetime.now() + timedelta(days=2), instructor="Bob", available_slots=10),
        models.FitnessClass(name="HIIT", datetime=datetime.now() + timedelta(days=3), instructor="Charlie", available_slots=2),
    ]
    db.add_all(classes)
    db.commit()
    db.close()

seed()