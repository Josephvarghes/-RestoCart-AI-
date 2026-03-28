from typing import Optional
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from db.session import SessionLocal
# from services.ai_service import AIService # Replacing this with AgentService
from services.ai.agent_service import AgentService

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class ChatRequest(BaseModel):
    question: str
    session_id: Optional[str] = "default_session"


class ChatResponse(BaseModel):
    answer: str



@router.post("/chat", response_model=ChatResponse)
def ai_chat(payload: ChatRequest, db: Session = Depends(get_db)):
    # answer = AIService.generate_answer(payload.question, AIService.search_products(db, payload.question))
    answer = AgentService.run_agent(db, payload.session_id, payload.question)
    return ChatResponse(answer=answer)
