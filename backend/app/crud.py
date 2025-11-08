from sqlalchemy.orm import Session

from app.core.security import get_password_hash
from app.models.user import User
from app.models.agent import Agent
from app.schemas.user import UserCreate
from app.schemas.agent import AgentCreate


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_agents(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Agent).offset(skip).limit(limit).all()


def get_agent(db: Session, agent_id: int):
    return db.query(Agent).filter(Agent.id == agent_id).first()


def create_agent(db: Session, agent: AgentCreate, owner_id: int):
    db_agent = Agent(**agent.dict(), owner_id=owner_id)
    db.add(db_agent)
    db.commit()
    db.refresh(db_agent)
    return db_agent
