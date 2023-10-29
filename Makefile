migrate:
	docker container exec -ti django_container python manage.py migrate
createsuperuser:
	docker container exec -ti django_container python manage.py createsuperuser
start:
	docker-compose up
	docker container exec -ti django_container python manage.py runserver
stop:
	docker-compose down
build:
	docker-compose build
shell:
	docker container exec -ti django_container python manage.py shell
precommit:
	docker container exec -ti django_container python -m flake8 .
	docker container exec -ti -u root django_container chown -R user:user /django

	docker container exec -ti django_container python -m blue .
	docker container exec -ti -u root django_container chown -R user:user /django

	docker container exec -ti django_container python -m isort . --skip migrations
	docker container exec -ti -u root django_container chown -R user:user /django
