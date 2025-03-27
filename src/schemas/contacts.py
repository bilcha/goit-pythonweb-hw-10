from pydantic import BaseModel, Field, ConfigDict
from src.conf import constants
from src.conf import messages
from typing import Optional
from datetime import date

class ContactSchema(BaseModel):
    first_name: str = Field(min_length=constants.NAME_MIN_LENGTH, max_length=constants.NAME_MAX_LENGTH, description=messages.contact_schema_first_name)
    last_name: str = Field(min_length=constants.NAME_MIN_LENGTH, max_length=constants.NAME_MAX_LENGTH, description=messages.contact_schema_last_name)
    email: str = Field(max_length=constants.EMAIL_MAX_LENGTH, description=messages.contact_schema_email)
    phone: str = Field(max_length=constants.PHONE_MAX_LENGTH, description=messages.contact_schema_phone)
    birthdate: date = Field(..., description=messages.contact_schema_bday)
    aditional_data: Optional[str] = Field(default=None, max_length=constants.ADDITIONAL_DATA_MAX_LENGTH, description=messages.contact_schema_additional_data)

class ContactUpdateSchema(BaseModel):
    first_name: Optional[str] = Field(default=None, min_length=constants.NAME_MIN_LENGTH, max_length=constants.NAME_MAX_LENGTH, description=messages.contact_schema_first_name)
    last_name: Optional[str] = Field(default=None, min_length=constants.NAME_MIN_LENGTH, max_length=constants.NAME_MAX_LENGTH, description=messages.contact_schema_last_name)
    email: Optional[str] = Field(default=None, max_length=constants.EMAIL_MAX_LENGTH, description=messages.contact_schema_email)
    phone: Optional[str] = Field(default=None, max_length=constants.PHONE_MAX_LENGTH, description=messages.contact_schema_phone)
    birthdate: Optional[date] = Field(default=None, description=messages.contact_schema_bday)
    aditional_data: Optional[str] = Field(default=None, max_length=constants.ADDITIONAL_DATA_MAX_LENGTH, description=messages.contact_schema_additional_data)   

class ContactResponseSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    phone: str
    birthdate: date
    aditional_data: Optional[str]
    
    model_config = ConfigDict(from_attributes=True)