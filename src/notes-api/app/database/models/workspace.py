"""
    Workspace database model.
"""

# ORM.
from sqlalchemy.sql import func
from sqlalchemy import (
    Integer, Column, DateTime, String
)

# Core model base.
from app.database.core import Base


class Workspace(Base):
    """ Workspace with notes. """
    __tablename__ = "workspaces"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    owner_id = Column(Integer, nullable=False)

    title = Column(String, nullable=False)
    
    time_created = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
