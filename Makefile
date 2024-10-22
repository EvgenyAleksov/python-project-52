install:
	poetry install

build: 
	poetry build

lint:
	poetry run flake8 task_manager

start:
	python manage.py runserver

deploy:
	poetry run gunicorn task_manager.wsgi
