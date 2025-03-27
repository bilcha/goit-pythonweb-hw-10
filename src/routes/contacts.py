import logging

from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.db import get_db
from services.contacts_service import ContactService
from src.schemas.contacts import (
    ContactResponseSchema,
    ContactSchema,
    ContactUpdateSchema
)


router = APIRouter(prefix="/contacts", tags=["contacts"])
logger = logging.getLogger("uvicorn.error")


@router.get("/", response_model=list[ContactResponseSchema])
async def get_contacts(
    limit: int = Query(10, ge=10, le=500),
    offset: int = Query(0, ge=0),
    first_name: str = Query(None, description="Filter by first name"),
    last_name: str = Query(None, description="Filter by last name"),
    email: str = Query(None, description="Filter by email"),
    db: AsyncSession = Depends(get_db),
):
    contact_service = ContactService(db)
    return await contact_service.get_contacts(limit, offset, first_name, last_name, email)


@router.get(
    "/{contact_id}",
    response_model=ContactResponseSchema,
    name="Get contact by id",
    description="Get contact by id",
    response_description="Contact details",
)
async def get_contact(contact_id: int, db: AsyncSession = Depends(get_db)):
    contact_service = ContactService(db)
    contact = await contact_service.get_contact(contact_id)
    if contact is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found"
        )
    return contact

@router.get(
    "/birthdays/next7days",
    response_model=list[ContactResponseSchema],
    name="Get contacts with birthdays in the next 7 days",
    description="Get contacts with birthdays in the next 7 days",
    response_description="List of contacts with upcoming birthdays",
)
async def get_contacts_with_upcoming_birthdays(db: AsyncSession = Depends(get_db)):
    contact_service = ContactService(db)
    return await contact_service.get_contacts_with_upcoming_birthdays()



@router.post(
    "/",
    response_model=ContactResponseSchema,
    status_code=status.HTTP_201_CREATED,
)
async def create_contact(body: ContactSchema, db: AsyncSession = Depends(get_db)):
    contact_service = ContactService(db)
    return await contact_service.create_contact(body)


@router.put("/{contact_id}", response_model=ContactResponseSchema)
async def update_contact(
    contact_id: int, body: ContactUpdateSchema, db: AsyncSession = Depends(get_db)
):
    contact_service = ContactService(db)
    contact = await contact_service.update_contact(contact_id, body)
    if contact is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found"
        )
    return contact


@router.delete("/{contact_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_contact(contact_id: int, db: AsyncSession = Depends(get_db)):
    contact_service = ContactService(db)
    await contact_service.remove_contact(contact_id)
    return None