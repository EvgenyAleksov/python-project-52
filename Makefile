PORT ?= 10000

MANAGE := poetry run python manage.py
RUN := poetry run

test:
	@poetry run pytest

setup: db-clean install migrate

install:
	@poetry install

db-clean:
	@rm db.sqlite3 || true

migrate:
	@$(MANAGE) migrate

shell:
	@$(MANAGE) shell_plus --ipython

lint:
	@poetry run flake8 task_manager

make dev:
	$(MANAGE) runserver

start:
	$(RUN) gunicorn --workers=5 --bind=0.0.0.0:$(PORT) task_manager.wsgi
