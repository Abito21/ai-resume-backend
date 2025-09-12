from agents import Agent, Runner
from loguru import logger
from sqlmodel import Session, select

from app.celery import app
from app.database.engine import engine
from app.database.models import ChatSession
from app.services.chatbot.chatbot_agents import (
    SYSTEM_PROMPT,
    query_resume,
)
from app.services.chatbot.chatbot_agents import (
    ChatSession as ChatSessionModel,
)
from app.utils.websocker_helper import publish_message


@app.task
def agent_task(chat_session_id: str, query: str):
    with Session(engine) as db:
        statement = select(ChatSession).where(ChatSession.id == chat_session_id)
        session = db.exec(statement).first()
        new_message = {"role": "user", "content": query}
        session.messages.append(new_message)
        messages = session.messages

        db.add(session)
        db.commit()
        db.refresh(session)

        logger.info(f"Messages: {messages}")
        chat_session = ChatSessionModel(id=chat_session_id)
        agent = Agent[ChatSessionModel](
            name="Resume Agent",
            model="gpt-4.1",
            instructions=SYSTEM_PROMPT,
            tools=[query_resume],
        )

        runner = Runner.run_sync(
            starting_agent=agent,
            input=messages,
            context=chat_session,
        )

        all_messages = runner.to_input_list()
        session.messages = all_messages
        db.add(session)
        db.commit()
        db.refresh(session)
        publish_message(chat_session_id, f"assistant<|>{runner.final_output}")
