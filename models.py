from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    password = Column(String, nullable=False)

    workspaces = relationship("Workspace", back_populates="owner")


class Workspace(Base):
    __tablename__ = "workspaces"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    blockchain = Column(String, nullable=False)

    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="workspaces")
    bots = relationship("Bot", back_populates="workspace")


class Bot(Base):
    __tablename__ = "bots"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)
    token = Column(String)
    chat_id = Column(String)
    mint_address = Column(String)
    status = Column(String, default="offline")

    workspace_id = Column(Integer, ForeignKey("workspaces.id"))

    workspace = relationship("Workspace", back_populates="bots")
