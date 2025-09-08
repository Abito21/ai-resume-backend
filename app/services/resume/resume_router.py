import os
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

@resume_router.post("/")
async def upload_resume(
    file: UploadFile,
    db: Session = Depends(db_session),
):
    contents = await file.read()
    original_filename = file.filename or "unknown_file.pdf"
    file_extension = os.path.splitext(original_filename)[1]

    file_path = f"public/resumes/{original_filename}"
    os.makedirs("public/resumes", exist_ok=True)
    with open(file_path, "wb") as f:
        f.write(contents)

    return { "message": "Resume uploaded successfully" }