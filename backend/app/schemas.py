from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class OrganizationCreate(BaseModel):
    name: str

class UserCreate(BaseModel):
    username: str
    organization_id: int

class MessageCreate(BaseModel):
    user_id: int
    content: str

class MessageOut(BaseModel):
    id: int
    user_id: int
    content: str
    timestamp: datetime
    class Config:
        orm_mode = True

class DocumentCreate(BaseModel):
    user_id: int
    title: str
    content: str

class DocumentOut(BaseModel):
    id: int
    title: str
    content: str
    class Config:
        orm_mode = True
