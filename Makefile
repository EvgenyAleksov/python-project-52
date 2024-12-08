PORT ?= 10000
MANAGE := poetry run python manage.py

.PHONY: install
install:
	@poetry install

.PHONY: test
test:
	@poetry run pytest

.PHONY: setup
setup: db-clean install migrate

.PHONY: db-clean
db-clean:
	@rm db.sqlite3 || true

.PHONY: migrate
migrate:
	@$(MANAGE) migrate

.PHONY: shell
shell:
	@$(MANAGE) shell_plus --ipython

.PHONY: lint
lint:
	ruff check task_manager  

dev:
	$(MANAGE) runserver

start:
	$(RUN) @poetry run gunicorn --workers=5 --bind=0.0.0.0:$(PORT) task_manager.wsgi
