# Fitness Studio Booking API

A simple FastAPI backend for booking fitness classes like Yoga, Zumba, and HIIT.

- `app/`: Contains FastAPI application code.
- `tests/`: Contains unit tests for the API.

## 🚀 Features

- View upcoming fitness classes
- Book a class with email
- View bookings by email
- Timezone-aware class times
- Error handling & logging
- Unit Testing
- MySQL backend

## ⚙️ Setup Instructions

1. **Clone the Repo**
```bash
git clone https://github.com/your-username/fitness-booking-api.git
cd fitness-booking-api
```

2. **Install Requirements**
```bash
pip install -r requirements.txt
```

3. **Update MySQL Config**
In `app/database.py`, update your MySQL credentials.

4. **Running Unit Tests**
- Run pytest with PYTHONPATH set
```bash
PYTHONPATH=. pytest tests/
```

5. **Run the App**
```bash
uvicorn app.main:app --reload
```

6. **Visit Swagger UI**
```
http://127.0.0.1:8000/docs
```

## 🧪 Sample Endpoints

### View Classes
```http
GET /classes?timezone=America/New_York
```

### Book Class
```http
POST /book
{
  "class_id": 1,
  "client_name": "John Doe",
  "client_email": "john@example.com"
}
```

### View Bookings
```http
GET /bookings?client_email=john@example.com
```

## ✅ Author

Created by Vedant Modi.