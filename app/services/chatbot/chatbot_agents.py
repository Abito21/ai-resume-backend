import json
from dataclasses import dataclass

from agents import RunContextWrapper, function_tool
from dotenv import load_dotenv

from app.modules.vector import query_resume_from_vector_db
from app.utils.websocker_helper import publish_message

load_dotenv()

SYSTEM_PROMPT = """ 
    You are an HR Resume Assistant that helps filter and evaluate candidates.

    RULES:
    - Always use query_resume to search the resume database
    - Base answers only on resume data from the database

    Your job: Help find the right candidates efficiently using resume data.
    """  # noqa


@dataclass
class ChatSession:
    id: str


@function_tool
def query_resume(
    wrapper: RunContextWrapper[ChatSession], query: str, n_results: int = 5
):
    publish_message(wrapper.context.id, "tool<|>Searching for candidates...")
    data = query_resume_from_vector_db(query, n_results=n_results)
    if data:
        publish_message(wrapper.context.id, "tool<|>Found candidates")
    else:
        publish_message(wrapper.context.id, "tool<|>No candidates found")
        return "No candidates found"

    return json.dumps(data)
