from pydantic import BaseModel, ConfigDict
from typing import Optional


class AgentBase(BaseModel):
    name: str
    description: Optional[str] = None
    category: Optional[str] = None
    icon_emoji: Optional[str] = None
    tags: Optional[str] = None
    primary_model: Optional[str] = None
    temperature: Optional[float] = 0.7
    max_tokens: Optional[int] = 2048
    reasoning_enabled: Optional[bool] = False
    system_prompt: Optional[str] = None


class AgentCreate(AgentBase):
    pass


class Agent(AgentBase):
    id: int
    owner_id: int

    model_config = ConfigDict(from_attributes=True)
