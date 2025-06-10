from enum import Enum
from typing import Optional
from uuid import UUID, uuid4
from sqlmodel import Field, Relationship, SQLModel


from .user import User
from .project import Project


class AccessLevel(str, Enum):
    VIEW = "VIEW"
    COMMENT = "COMMENT"
    EDIT = "EDIT"
    MANAGE = "MANAGE"


class TeamRole(str, Enum):
    LEAD = "LEAD"
    MEMBER = "MEMBER"
    REVIEWER = "REVIEWER"


class Team(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str = Field(index=True)
    purpose: Optional[str] = None

    # Relationship
    project: List["ProjectTeam"] = Relationship(back_populates="team")
    team_members: List["TeamMember"] = Relationship(back_populates="team")


class ProjectTeam(SQLModel, table=True):
    project_id: UUID = Field(foreign_key="project.id", primary_key=True)
    team_id: UUID = Field(foreign_key="team.id", primary_key=True)
    access_level: AccessLevel = Field(index=True)

    # Relationships
    project: "Project" = Relationship(back_populates="project_teams")
    team: Team = Relationship(back_populates="project_teams")


class TeamMember(SQLModel, table=True):
    team_id: UUID = Field(foreign_key="team.id", primary_key=True)
    user_id: UUID = Field(foreign_key="user.id", primary_key=True)
    role: TeamRole = Field(index=True)

    # Relationships
    team: Team = Relationship(back_populates="team_members")
    user: User = Relationship(back_populates="team_memberships")
