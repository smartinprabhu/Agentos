from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.core.database import Base


class Agent(Base):
    __tablename__ = "agents"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    category = Column(String)
    icon_emoji = Column(String)
    tags = Column(String)
    primary_model = Column(String)
    temperature = Column(Float)
    max_tokens = Column(Integer)
    reasoning_enabled = Column(Boolean)
    system_prompt = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="agents")
