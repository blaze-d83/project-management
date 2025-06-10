from enum import Enum
from uuid import UUID, uuid4
from datetime import date, datetime
from .user import User

from sqlmodel import Field, Relationship, SQLModel


class TaskStatus(str, Enum):
    NOT_STARTED = "NOT_STARTED"
    IN_PROGRESS = "IN_PROGRESS"
    BLOCKED = "BLOCKED"
    COMPLETE = "COMPLETE"


class TaskPriority(str, Enum):
    CRITICAL = "CRITICAL"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"


class Task(SQLModel, table=True):
    pass


class TimeEntry(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    task_id: UUID = Field(foreign_key="task.id", index=True)
    user_id: UUID = Field(foreign_key="user.id", index=True)
    duration: int
    date: date
    description: str
    billable: bool = Field(default=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    # Relationsships
    task: Task = Relationship(back_populates="time_entries")
    user: User = Relationship(back_populates="time_entries")
