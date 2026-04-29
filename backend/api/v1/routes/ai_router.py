from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from db.session import SessionLocal
from repositories.chat_repo import ChatRepository
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
    session_id: str


class ChatResponse(BaseModel):
    answer: str


class MessageSchema(BaseModel):
    role: str
    content: str

    class Config:
        from_attributes = True


@router.post("/chat", response_model=ChatResponse)
async def ai_chat(payload: ChatRequest, db: Session = Depends(get_db)):
    answer = await AgentService.run_agent(db, payload.session_id, payload.question)
    return ChatResponse(answer=answer)


@router.get("/history/{session_id}", response_model=list[MessageSchema])
def get_chat_history(session_id: str, db: Session = Depends(get_db)):
    history = ChatRepository.get_history(db, session_id)
    return history
