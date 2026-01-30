from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from . import models, schemas
from app import models, schemas

# Create organization
async def create_organization(db: AsyncSession, org: schemas.OrganizationCreate):
    db_org = models.Organization(name=org.name)
    db.add(db_org)
    await db.commit()
    await db.refresh(db_org)
    return db_org

# Create user
async def create_user(db: AsyncSession, user: schemas.UserCreate):
    db_user = models.User(username=user.username, organization_id=user.organization_id)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

# Create message
async def create_message(db: AsyncSession, msg: schemas.MessageCreate):
    db_msg = models.Message(user_id=msg.user_id, content=msg.content)
    db.add(db_msg)
    await db.commit()
    await db.refresh(db_msg)
    return db_msg

# Get messages for a user
async def get_messages(db: AsyncSession, user_id: int):
    result = await db.execute(select(models.Message).where(models.Message.user_id==user_id))
    return result.scalars().all()

# Create document
async def create_document(db: AsyncSession, doc: schemas.DocumentCreate):
    db_doc = models.Document(user_id=doc.user_id, title=doc.title, content=doc.content)
    db.add(db_doc)
    await db.commit()
    await db.refresh(db_doc)
    return db_doc

# Get documents for a user
async def get_documents(db: AsyncSession, user_id: int):
    result = await db.execute(select(models.Document).where(models.Document.user_id==user_id))
    return result.scalars().all()
