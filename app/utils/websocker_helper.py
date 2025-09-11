import asyncio
import json

from app.utils.redis_client import redis_client
from app.websocket import manager


async def redis_listener():
    pubsub = redis_client.pubsub()
    await asyncio.to_thread(pubsub.subscribe, "notifications")

    while True:
        try:
            message = await asyncio.to_thread(pubsub.get_message, timeout=1.0)
            if message and message["type"] == "message":
                data = json.loads(message["data"])
                await manager.send_to_channel(data["channel"], data["message"])
        except Exception as e:
            print(f"Redis listener error: {e}")
            await asyncio.sleep(1)


def publish_message(channel: str, message: str):
    data = {"channel": channel, "message": message}
    redis_client.publish("notifications", json.dumps(data))