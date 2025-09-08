from fastapi import APIRouter, Depends, UploadFile
from sqlmodel import Session, select, desc
from app.database.models import Resume
from app.database.engine import db_session

resume_router = APIRouter(prefix="/resume", tags=["resume"])

@resume_router.get("/")
async def get_resumes(
    db: Session = Depends(db_session),
):
    statement = select(Resume).order_by(desc(Resume.created_at))
    resumes = db.exec(statement).all()
    return resumes