from sqlalchemy import create_engine, Column, Integer, String, Date, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import settings

# Database URL from settings
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

# Create the database engine and session
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for declarative models
Base = declarative_base()

# User model definition
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

# Function to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Entry model definition
class Entry(Base):
    __tablename__ = "entries"

    id = Column(Integer, primary_key=True, index=True)
    # entry_type = Column(String)  # Either 'Professional' or 'Educational'
    # description = Column(String)  # Work/Project/Duration
    date = Column(Date)  # Date
    company_name = Column(String)  # Company Name
    keyword = Column(String)  # Keyword
    detail_description = Column(String)  # Detail Description

# Create tables if not exist
Base.metadata.create_all(bind=engine)

class File(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    data = Column(LargeBinary)

