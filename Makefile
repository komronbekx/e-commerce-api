.PHONY: setup dev format lint typecheck test lint-deps check-migration ci pre-prod stop

setup:
	uv run manage.py makemigrations
	uv run manage.py migrate
	uv run manage.py createcachetable
	uv run manage.py createsuperuser

dev:
	uv run manage.py runserver 0.0.0.0:8000

format:
	uv run ruff check . --fix
	uv run black .

lint:
	uv run ruff check .
	uv run black --check .

typecheck:
	uv run mypy .

test:
	uv run pytest

lint-deps:
	uv run deptry .

check-migration:
	uv run manage.py makemigrations --check --dry-run

ci: lint typecheck test lint-deps check-migration

pre-prod:
	docker compose -f docker/docker-compose.yaml up --build

stop:
	docker compose -f docker/docker-compose.yaml down