from fastapi import FastAPI, Depends , HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from . import models, schemas, crud, database, ai

import asyncio

app = FastAPI(title="AI Chat Application")

# Create tables
@app.on_event("startup")
async def startup():
    async with database.engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)

# Organizations
@app.post("/organizations/", response_model=schemas.OrganizationCreate)
async def create_organization(org: schemas.OrganizationCreate, db: AsyncSession = Depends(database.get_db)):
    return await crud.create_organization(db, org)

# Users
@app.post("/users/", response_model=schemas.UserCreate)
async def create_user(user: schemas.UserCreate, db: AsyncSession = Depends(database.get_db)):
    return await crud.create_user(db, user)

# Messages
@app.post("/messages/", response_model=schemas.MessageOut)
async def create_message(msg: schemas.MessageCreate, db: AsyncSession = Depends(database.get_db)):
    return await crud.create_message(db, msg)

@app.get("/messages/{user_id}", response_model=List[schemas.MessageOut])
async def get_messages(user_id: int, db: AsyncSession = Depends(database.get_db)):
    return await crud.get_messages(db, user_id)

# Documents
@app.post("/documents/", response_model=schemas.DocumentOut)
async def create_document(doc: schemas.DocumentCreate, db: AsyncSession = Depends(database.get_db)):
    db_doc = await crud.create_document(db, doc)
    docs = await crud.get_documents(db, doc.user_id)
    ai.add_documents(doc.user_id, [{"title": d.title, "content": d.content} for d in docs])
    return db_doc

@app.get("/documents/{user_id}", response_model=List[schemas.DocumentOut])
async def get_documents(user_id: int, db: AsyncSession = Depends(database.get_db)):
    return await crud.get_documents(db, user_id)

# Chat
@app.post("/chat/")
async def chat_endpoint(user_id: int, query: str):
    response = ai.chat(user_id, query)
    return {"response": response}
