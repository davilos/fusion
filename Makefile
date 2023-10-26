migrate:
	docker container exec -ti django_container python manage.py migrate
createsuperuser:
	docker container exec -ti django_container python manage.py createsuperuser
start:
	docker-compose up
stop:
	docker-compose down
build:
	docker-compose build
shell:
	docker container exec -ti django_container python manage.py shell
