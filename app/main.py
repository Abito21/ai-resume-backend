from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from scalar_fastapi.scalar_fastapi import get_scalar_api_reference

from app.core.settings import settings

app = FastAPI(
    title=settings.app.APP_NAME,
    version=settings.app.VERSION
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors.ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("scalar", include_in_schema=False)
async def scalar():
    return get_scalar_api_reference(
        openapi_url=settings.app.OPENAPI_URL,
        title=settings.app.APP_NAME
    )