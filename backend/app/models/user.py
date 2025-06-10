from typing import List, Optional
from uuid import uuid4
from pydantic import EmailStr
from sqlmodel import UUID, Field, Relationship, SQLModel
from enum import Enum


class UserRole(str, Enum):
    ADMIN = "ADMIN"
    MANAGER = "MANAGER"
    CONTRIBUTOR = "CONTRIBUTER"


class User(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    bar_number: Optional[str] = Field(index=True, unique=True)
    first_name: str
    last_name: str
    email: EmailStr = Field(index=True, unique=True)
    role: UserRole = Field(index=True)
    timezone: str = Field(default="UTC")

    created_tasks: List["Task"] = Relationship(
        back_populates="created_by",
        sa_relationship_kwargs={"foreign_keys": "Task.created_by_id"},
    )

    assigned_tasks: List["Task"] = Relationship(
        back_populates="assigned_to",
        sa_relationship_kwargs={"foreign_keys": "Task.created_by_id"},
    )

    time_entries: List["TimeEntry"] = Relationship(back_populates="user")
    documents: List["Document"] = Relationship(back_populates="created_by")
    team_memberships: List["TeamMember"] = Relationship(back_populates="user")
