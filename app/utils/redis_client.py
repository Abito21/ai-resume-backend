import json

import redis

from app.core.settings import settings

redis_client = redis.Redis(
    host=settings.database.REDIS_HOST,
    port=settings.database.REDIS_PORT,
    decode_responses=True,
)


def set_memory(id: str, content: dict) -> bool:
    try:
        key = f"memory_{id}"
        json_content = json.dumps(content)
        return redis_client.set(key, json_content)
    except Exception:
        return False


def delete_memory(id: str) -> bool:
    try:
        key = f"memory_{id}"
        redis_client.delete(key)
        return True
    except Exception:
        return False


def get_memory(id: str) -> dict | None:
    try:
        key = f"memory_{id}"
        json_content = redis_client.get(key)
        if json_content is None:
            return None
        return json.loads(json_content)
    except Exception:
        return None


def get_chat_history(chat_session_id: str) -> list:
    memory = get_memory(chat_session_id)
    if memory and "messages" in memory:
        return memory["messages"]
    return []