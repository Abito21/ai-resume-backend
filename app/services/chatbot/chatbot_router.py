from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import load_only
from sqlmodel import Session, desc, select

from app.database.engine import db_session
from app.database.models import ChatSession
from app.services.chatbot.chatbot_schema import ChatbotSchema
from app.services.chatbot.chatbot_tasks import agent_task

chatbot_router = APIRouter(prefix="/chatbot", tags=["chatbot"])


@chatbot_router.get("/")
async def get_chatbot_sessions(db: Session = Depends(db_session)):
    statement = (
        select(ChatSession)
        .options(load_only(ChatSession.id, ChatSession.chat_title))
        .order_by(desc(ChatSession.created_at))
    )
    sessions = db.exec(statement).all()
    return [
        {"id": session.id, "chat_title": session.chat_title} for session in sessions
    ]


@chatbot_router.post("/")
async def create_session(db: Session = Depends(db_session)):
    session = ChatSession(chat_title="New Chat")
    db.add(session)
    db.commit()
    db.refresh(session)
    return {"id": session.id, "chat_title": session.chat_title}


@chatbot_router.get("/{chat_session_id}")
async def get_session(chat_session_id: str, db: Session = Depends(db_session)):
    statement = select(ChatSession).where(ChatSession.id == chat_session_id)
    session = db.exec(statement).first()
    if session:
        return session

    raise HTTPException(status_code=404, detail="Session not found")


@chatbot_router.post("/{chat_session_id}")
async def query_chatbot(input: ChatbotSchema, chat_session_id: str):
    agent_task.delay(chat_session_id, input.query)
    return {"message": "Query received"}
