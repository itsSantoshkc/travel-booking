run:
	python manage.py runserver

migrate:
	python manage.py migrate

migrations:
	python manage.py makemigrations

shell:
	python manage.py shell

superuser:
	python manage.py createsuperuser

collectstatic:
	python manage.py collectstatic --noinput

freeze:
	pip freeze > requirements.txt

install:
	pip install -r requirements.txt

# docker-up:
# 	docker compose up --build

# docker-down:
# 	docker compose down