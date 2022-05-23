"""
    Note database model.
"""

# ORM.
from sqlalchemy.sql import func
from sqlalchemy import (
    Integer, Column, DateTime, Text, ForeignKey
)

# Core model base.
from app.database.core import Base


class Note(Base):
    """ Note main element. """
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    workspace_id = Column(Integer, ForeignKey("workspaces.id"), nullable=False)

    text = Column(Text, nullable=False)

    time_created = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
