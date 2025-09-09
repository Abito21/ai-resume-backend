format:
	uv run ruff format .
	uv run ruff check . --fix

dev:
	uv run uvicorn app.main:app --reload

worker:
	uv run celery -A app.celery.app worker --pool=solo -c 1 --loglevel=info
# 	uv run celery -A app.celery.app worker -c 1