"""
SQLAlchemy models representing FitnessClass and Booking tables.
"""

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class FitnessClass(Base):
    __tablename__ = "classes"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    datetime = Column(DateTime, nullable=False)
    instructor = Column(String(100), nullable=False)
    available_slots = Column(Integer, default=0)
    bookings = relationship("Booking", back_populates="fitness_class")

class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True, index=True)
    class_id = Column(Integer, ForeignKey("classes.id"))
    client_name = Column(String(100), nullable=False)
    client_email = Column(String(100), nullable=False)
    fitness_class = relationship("FitnessClass", back_populates="bookings")