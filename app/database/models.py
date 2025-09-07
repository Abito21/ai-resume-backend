from enum import Enum
from typing import Any, Dict, List, Optional

from sqlmodel import JSON, Column, Field

from app.core.base_models import BaseModel


class ResumeStatus(str, Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"


class Resume(BaseModel, table=True):
    fullname: Optional[str] = Field("")
    email: Optional[str] = Field("")
    phone: Optional[str] = Field("")
    address: Optional[str] = Field("")
    category: Optional[str] = Field("")
    summary: Optional[str] = Field("")
    raw_resume: Optional[str] = Field("")
    file_name: Optional[str] = Field("")
    file_path: Optional[str] = Field("")
    status: ResumeStatus = Field(default=ResumeStatus.PENDING)
    skills: Optional[List[str]] = Field(default_factory=list, sa_column=Column(JSON))
    strength: Optional[List[str]] = Field(default_factory=list, sa_column=Column(JSON))


class ChatSession(BaseModel, table=True):
    chat_title: Optional[str] = Field("New Chat Session")
    messages: Optional[List[Dict[str, Any]]] = Field(
        default_factory=list, sa_column=Column(JSON)
    )
    history: Optional[List[Dict[str, Any]]] = Field(
        default_factory=list, sa_column=Column(JSON)
    )
