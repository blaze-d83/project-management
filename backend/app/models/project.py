from datetime import date, datetime
from enum import Enum
from typing import Any, Dict, Optional
from uuid import UUID, uuid4
from sqlmodel import Field, Relationship, SQLModel


class ProjectStatus(str, Enum):
    PLANNING = "PLANNING"
    ACTIVE = "ACTIVE"
    HOLD = "HOLD"
    COMPLETED = "COMPLETED"


class DeadlineType(str, Enum):
    COURT = "COURT"
    STATUTORY = "STATUTORY"
    INTERNAL = "INTERNAL"
    CLIENT = "CLIENT"


class Project(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    title: str = Field(index=True)
    description: Optional[str] = None
    status: ProjectStatus = Field(index=True)
    start_date: date
    target_date: Optional[date] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    # Relationships
    deadlines: List["Deadline"] = Relationship(back_populates="project")
    custom_fields: List["ProjectCustomField"] = Relationship(back_populates="project")
    tasks: List["Task"] = Relationship(back_populates="project")
    documents: List["Document"] = Relationship(back_populates="project")
    project_tags: List["ProjectTag"] = Relationship(back_populates="project")
    project_teams: List["ProjectTeam"] = Relationship(back_populates="project")


class ProjectCustomField(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    project_id: UUID = Field(foreign_key="project.id", index=True)
    field_name: str = Field(index=True)
    field_type: str = Field(index=True)
    field_value: str

    # Relationship
    project: Project = Relationship(back_populates="custom_fields")


class Deadline(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    project_id: UUID = Field(foreign_key=uuid4, primary_key=True)
    title: str
    due_date: datetime
    deadline_type: DeadlineType = Field(index=True)
    remainder_strategy: Dict[str, Any] = Field(
        default={}, sa_column_kwargs={"type": "JSONB"}
    )
    project: Project = Relationship(back_populates="deadlines")
