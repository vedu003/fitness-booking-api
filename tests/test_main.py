"""
Unit tests for the Fitness Studio Booking API.
"""

import sys
import os

# Add the project root to sys.path so 'app' is found
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_classes():
    """Test fetching available classes (default timezone)."""
    response = client.get("/classes")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_classes_invalid_timezone():
    """Test fetching classes with invalid timezone."""
    response = client.get("/classes?timezone=Invalid/Zone")
    assert response.status_code == 400
    assert response.json()["message"] == "Invalid timezone"

def test_booking_and_retrieval():
    """Test booking a class and retrieving the booking."""
    # Book a class
    booking_data = {
        "class_id": 1,
        "client_name": "Test User",
        "client_email": "testuser@example.com"
    }
    response = client.post("/book", json=booking_data)
    assert response.status_code == 200
    booking = response.json()
    assert booking["client_email"] == "testuser@example.com"

    # Retrieve bookings
    response = client.get("/bookings", params={"client_email": "testuser@example.com"})
    assert response.status_code == 200
    bookings = response.json()
    assert any(b["client_email"] == "testuser@example.com" for b in bookings)