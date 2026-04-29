from uuid import UUID
from datetime import datetime
import uuid_utils as uuid7
from sqlalchemy import Boolean, DateTime, ForeignKey, String, Text, func
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class User(Base):
    __tablename__ = "user"

    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid = True),
        primary_key= True,
        default= uuid7.uuid7,
    )
    username: Mapped[str] = mapped_column(
        String(50),
        unique = True,
        nullable= False,
    )
    email: Mapped[str] = mapped_column(
        String(255),
        unique= True,
        nullable= False,
    )

    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable= False,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default= True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default= func.now(),
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone= True),
        default = func.now(),
        onupdate=func.now(),
    )

    owned_teams = relationship("Team", back_populates="owner")

class Team(Base):
    __tablename__ = "team"

    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid= True),
        primary_key= True,
        default= uuid7.uuid7,
    )

    name: Mapped[str] = mapped_column(
        String(50),
        unique= True,
        nullable= False,
    )

    owner_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid= True),
        ForeignKey("user.id"),
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone= True),
        default= func.now(),
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default = func.now(),
        onupdate=func.now(),
    )

    owner = relationship("User", back_populates= "owned_teams")

class TeamMember(Base):
    __tablename__ = "team_member"

    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid= True),
        primary_key= True,
        default= uuid7.uuid7,
    )

    team_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid= True),
        ForeignKey("team.id"),
        nullable = False
    )

    user_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("user.id"),
        nullable= False,
    )

    role: Mapped[str] = mapped_column(
        String(50),
    )

    joined_at: Mapped[datetime] = mapped_column(
        DateTime(timezone= True),
        default = func.now(),
    )
    team = relationship("Team", foreign_keys=[team_id])
    user = relationship("User", foreign_keys=[user_id])

class Task(Base):
    __tablename__ = "task"

    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid= True),
        primary_key= True,
        default = uuid7.uuid7,
    )

    title: Mapped[str] = mapped_column(
        String(50),
        nullable= False,
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable= True,
    )

    team_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid= True),
        ForeignKey("team.id"),
        nullable = False
    )

    creator_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid= True),
        ForeignKey("user.id"),
        nullable= False,
    )

    assignee_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid= True),
        ForeignKey("user.id"),
        nullable =True
    )

    status: Mapped[str] = mapped_column(
        String(30),
        nullable= False
    )

    priority: Mapped[str] = mapped_column(
        String(20),
        nullable= True,
    )

    due_date: Mapped[datetime] = mapped_column(
        DateTime(timezone= True),
        nullable= True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone = True),
        nullable= False,
        default = func.now(),
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone= True),
        default = func.now(),
        onupdate=func.now(),
    )

    team = relationship("Team", foreign_keys=[team_id])
    creator = relationship("User", foreign_keys=[creator_id])
    assignee = relationship("User", foreign_keys=[assignee_id])

class Comment(Base):
    __tablename__ = "comment"

    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid= True),
        primary_key= True,
        default= uuid7.uuid7,
    )

    task_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("task.id"),
        nullable= False,
    )

    user_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid= True),
        ForeignKey("user.id"),
        nullable= False,
    )

    content: Mapped[str] = mapped_column(
        Text,
        nullable= False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default = func.now(),
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default = func.now(),
        onupdate=func.now(),
    )
    task = relationship("Task", foreign_keys=[task_id])
    user = relationship("User", foreign_keys=[user_id])


class TaskHistory(Base):
    __tablename__ = "task_history"

    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid= True),
        primary_key= True,
        default= uuid7.uuid7,
    )

    task_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid= True),
        ForeignKey("task.id"),
        nullable= False,
    )

    user_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("user.id"),
        nullable=False,
    )

    action_type: Mapped[str] = mapped_column(
        String(50),
        nullable= False,
    )

    old_value: Mapped[str] = mapped_column(
        Text,
        nullable= False,
    )

    new_value: Mapped[str] = mapped_column(
        Text,
        nullable= False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone= True),
        default= func.now(),
    )
    task = relationship("Task", foreign_keys=task_id)
    user = relationship("User", foreign_keys= user_id)

