from uuid import uuid4
from pydantic import EmailStr
from sqlmodel import UUID, Field, SQLModel


class Client(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    first_name: str
    last_name: str
    email: EmailStr
    address: str
    phone1: str
    phone2: str
