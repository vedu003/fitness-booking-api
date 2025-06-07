"""
Database configuration using SQLAlchemy with MySQL.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
import urllib.parse

# Update with your actual DB credentials
DB_USER = "root"
DB_PASSWORD = urllib.parse.quote_plus("P@ssw0rd@123")  # encodes @, :, etc.
DB_HOST = "localhost"
DB_PORT = 3306
DB_NAME = "fitnessdb"

# Construct the full DB URL
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# SQLAlchemy setup
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()