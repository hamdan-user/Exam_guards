from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Entry schema
class EntryCreate(BaseModel):
    # entry_type: str  # Professional or Educational
    # description: str
    date: date
    company_name: str
    keyword: Optional[str] = None
    detail_description: Optional[str] = None

    class Config:
        from_attributes = True

class EntryResponse(BaseModel):
    id: int
    date: date
    company_name: str
    keyword: str
    detail_description: str

    class Config:
        from_attributes = True        