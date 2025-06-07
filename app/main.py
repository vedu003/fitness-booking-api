from fastapi import FastAPI, Depends, HTTPException, Query, Request
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from .database import SessionLocal
from . import crud, schemas
from .logger import logger
from zoneinfo import ZoneInfo

app = FastAPI(title="Fitness Studio Booking API", version="1.0")

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Custom Exception Handlers
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    logger.warning(f"HTTPException: {exc.detail} at {request.url}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"status": "error", "message": exc.detail},
    )

@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled Exception: {str(exc)} at {request.url}")
    return JSONResponse(
        status_code=500,
        content={"status": "error", "message": "Internal server error"},
    )

@app.get("/classes", response_model=list[schemas.ClassOut])
def get_classes(
    db: Session = Depends(get_db),
    timezone: str = Query("Asia/Kolkata", description="Your timezone (e.g., America/New_York)")
):
    """
    Get all available fitness classes with datetime converted to the requested timezone.
    """

    classes = crud.get_classes(db)
    try:
        tz = ZoneInfo(timezone)
    except Exception as e:
        logger.warning(f"Invalid timezone '{timezone}'")
        raise HTTPException(status_code=400, detail="Invalid timezone")

    # Convert each class datetime to requested timezone
    for c in classes:
        c.datetime = c.datetime.astimezone(tz)
    logger.info(f"Returned {len(classes)} classes in timezone {timezone}")
    return classes

@app.post("/book", response_model=schemas.BookingOut)
def book_class(booking: schemas.BookingIn, db: Session = Depends(get_db)):
    """
    Book a spot in a class if slots are available.
    """
    logger.info(f"Booking attempt by {booking.client_email} for class_id {booking.class_id}")
    return crud.create_booking(db, booking)

@app.get("/bookings", response_model=list[schemas.BookingOut])
def get_bookings(client_email: str, db: Session = Depends(get_db)):
    """
    Get all bookings made by a specific email address.
    """
    bookings = crud.get_bookings_by_email(db, client_email)
    logger.info(f"{len(bookings)} bookings fetched for {client_email}")
    return crud.get_bookings_by_email(db, client_email)
