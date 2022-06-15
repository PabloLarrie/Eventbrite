up:
	docker-compose up

down:
	docker-compose down

pip-compile:
	docker-compose run eventbrite pip-compile requirements.in > requirements.txt

shell:
	docker-compose run eventbrite python manage.py shell

chown:
	sudo chown `whoami` -R .

freeze_dependencies: pip-compile chown

build:
	docker-compose build

migrate:
	docker-compose run eventbrite python manage.py migrate

migrations:
	docker-compose run eventbrite python manage.py makemigrations

dumpevents:
	docker-compose run eventbrite python manage.py dumpdata events.Event -o backend/events/fixtures/events.json --indent 4

dumptickets:
	docker-compose run eventbrite python manage.py dumpdata events.Ticket -o backend/events/fixtures/tickets.json --indent 4

dumplocations:
	docker-compose run eventbrite python manage.py dumpdata events.Location -o backend/events/fixtures/locations.json --indent 4

loaddata:
	docker-compose run eventbrite python manage.py loaddata backend/events/fixtures/*
