from sqlalchemy.ext.asyncio import AsyncSession
from datetime import date, timedelta
from src.entity.models import User

from src.repositories.contacts_repo import ContactRepository
from src.schemas.contacts import ContactSchema, ContactUpdateSchema


class ContactService:
    def __init__(self, db: AsyncSession):
        self.contact_repository = ContactRepository(db)

    async def create_contact(self, body: ContactSchema, user: User):
        return await self.contact_repository.create_contact(body, user)

    async def get_contacts(self, limit: int, offset: int, user: User):
        return await self.contact_repository.get_contacts(limit, offset, user)

    async def get_contact(self, contact_id: int, user: User):
        return await self.contact_repository.get_contact_by_id(contact_id, user)

    async def update_contact(self, contact_id: int, body: ContactUpdateSchema, user: User):
        return await self.contact_repository.update_contact(contact_id, body, user)

    async def remove_contact(self, contact_id: int, user: User):
        return await self.contact_repository.remove_contact(contact_id, user)
    
    async def get_contacts_with_upcoming_birthdays(self):
        today = date.today()
        next_week = today + timedelta(days=7)
        return await self.contact_repository.get_contacts_with_birthdays_between(today, next_week)