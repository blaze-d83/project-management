from datetime import datetime
from enum import Enum
from typing import Optional
from uuid import UUID, uuid4
from sqlmodel import Field, Relationship, SQLModel

from .project import Project
from .task import Task
from .user import User


class DocumentCategory(str, Enum):
    PLEADING = "PLEADING"
    CONTRACT = "CONTRACT"
    EVIDENCE = "EVIDENCE"
    RESEARCH = "RESEARCH"
    CORRESPONDENCE = "CORRESPONDENCE"
    DISCOVERY = "DISCOVERY"


class Document(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    project_id: UUID = Field(foreign_key="project.id", index=True)
    task_id: Optional[UUID] = Field(foreign_key="task.id", index=True)
    filename: str
    storage_key: str
    version: int = Field(default=1)
    category: Optional[DocumentCategory] = Field(index=True)
    created_by_id: UUID = Field(foreign_key="user.id")
    created_at: datetime = Field(default_factory=datetime.utcnow)

    # Relationships
    project: Project = Relationship(back_populates="documents")
    task: Optional[Task] = Relationship(back_populates="documents")
    created_user: User = Relationship(back_populates="documents")
