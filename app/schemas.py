"""
Pydantic schemas for request and response models.
"""

from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List

class ClassBase(BaseModel):
    name: str
    datetime: datetime
    instructor: str
    available_slots: int

class ClassOut(ClassBase):
    id: int
    class Config:
        from_attributes = True

class BookingIn(BaseModel):
    class_id: int
    client_name: str
    client_email: EmailStr

class BookingOut(BaseModel):
    id: int
    class_id: int
    client_name: str
    client_email: EmailStr
    class Config:
        from_attributes = True
