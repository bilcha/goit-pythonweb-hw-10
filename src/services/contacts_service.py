from sqlalchemy.ext.asyncio import AsyncSession
from datetime import date, timedelta

from src.repositories.contacts_repo import ContactRepository
from src.schemas.contacts import ContactSchema, ContactUpdateSchema


class ContactService:
    def __init__(self, db: AsyncSession):
        self.contact_repository = ContactRepository(db)

    async def create_contact(self, body: ContactSchema):
        return await self.contact_repository.create_contact(body)

    async def get_contacts(self, limit: int, offset: int, first_name: str = None, last_name: str = None, email: str = None):
        return await self.contact_repository.get_contacts(limit, offset, first_name, last_name, email)

    async def get_contact(self, contact_id: int):
        return await self.contact_repository.get_contact_by_id(contact_id)

    async def update_contact(self, contact_id: int, body: ContactUpdateSchema):
        return await self.contact_repository.update_contact(contact_id, body)

    async def remove_contact(self, contact_id: int):
        return await self.contact_repository.remove_contact(contact_id)
    
    async def get_contacts_with_upcoming_birthdays(self):
        today = date.today()
        next_week = today + timedelta(days=7)
        return await self.contact_repository.get_contacts_with_birthdays_between(today, next_week)