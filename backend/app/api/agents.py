from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud
from app.api import deps
from app.core.database import get_db
from app.models.user import User
from app.schemas.agent import Agent, AgentCreate

router = APIRouter()


@router.get("/", response_model=List[Agent])
def read_agents(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(deps.get_current_user),
):
    agents = crud.get_agents(db, skip=skip, limit=limit)
    return agents


@router.post("/", response_model=Agent)
def create_agent(
    agent: AgentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(deps.get_current_user),
):
    return crud.create_agent(db=db, agent=agent, owner_id=current_user.id)


@router.get("/{agent_id}", response_model=Agent)
def read_agent(
    agent_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(deps.get_current_user),
):
    db_agent = crud.get_agent(db, agent_id=agent_id)
    if db_agent is None:
        raise HTTPException(status_code=404, detail="Agent not found")
    return db_agent
