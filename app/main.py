import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from scalar_fastapi import get_scalar_api_reference

from app.core.settings import settings
from app.services.chatbot.chatbot_router import chatbot_router
from app.services.resume.resume_router import resume_router
from app.utils.redis_client import redis_client
from app.utils.websocker_helper import redis_listener
from app.websocket import manager


@asynccontextmanager
async def lifespan(app: FastAPI):
    task = asyncio.create_task(redis_listener())
    yield
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        pass
    redis_client.close()


app = FastAPI(
    title=settings.app.APP_NAME,
    version=settings.app.VERSION,
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors.ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/public", StaticFiles(directory="public"), name="public")
app.include_router(resume_router)
app.include_router(chatbot_router)


@app.websocket("/ws/{channel}")
async def websocket_endpoint(websocket: WebSocket, channel: str):
    await manager.connect(websocket, channel)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_to_channel(channel, data)
    except WebSocketDisconnect:
        await manager.disconnect(websocket, channel)


@app.get("/health")
async def check_health():
    return {"health": "ok"}


@app.get("/scalar", include_in_schema=False)
async def scalar():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title,
    )
