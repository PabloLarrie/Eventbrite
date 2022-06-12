up:
	docker-compose up

down:
	docker-compose down

dest:
	docker exec -it hsdecker_postgres_1 bash

test:
	docker-compose run eventbrite pytest -c pytest.ini

pip-compile:
	docker-compose run eventbrite pip-compile requirements.in > requirements.txt

shell:
	docker-compose run eventbrite python manage.py shell

shell+:
	docker-compose run eventbrite python manage.py shell_plus

chown:
	sudo chown `whoami` -R .

freeze_dependencies: pip-compile chown

run:
	docker-compose run eventbrite python manage.py runserver

build:
	docker-compose build

migrate:
	docker-compose run eventbrite python manage.py migrate

migrations:
	docker-compose run eventbrite python manage.py makemigrations

manage:
	docker-compose run eventbrite python manage.py $(c)


#installfrontend:
#	${DOCKER_FRONTEND} npm install
#
#installvuestrap:
#	${DOCKER_FRONTEND} npm install vue bootstrap bootstrap-vue
#
#addvuestrap:
#	${DOCKER_FRONTEND} vue add bootstrap-vue
#
#installrouter:
#	${DOCKER_FRONTEND} npm install vue-router
#
#vuestrap: installvuestrap addvuestrap
