from sqlalchemy.orm import Session
from models.chat_model import ChatMessage

class ChatRepository:
    @staticmethod
    def add_message(db: Session, session_id: str, role: str, content: str):
        message = ChatMessage(session_id=session_id, role=role, content=content)
        db.add(message)
        db.commit()
        db.refresh(message)
        return message

    @staticmethod
    def get_history(db: Session, session_id: str, limit: int = 10):
        return (
            db.query(ChatMessage)
            .filter(ChatMessage.session_id == session_id)
            .order_by(ChatMessage.created_at.asc())
            .limit(limit)
            .all()
        )
