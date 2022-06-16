Stores from different countries small example
=========================================================

## Coments:

* About me
* About this code
* Part 1 - Creating the Backend
* Part 2 - File Ingestion
* Part 3 - Creating the Frontend
* Part 4 - Running the code


## About me

I first met coding in November 2020. At that time, it started just being another hobby more. But slowly, I dedicated more and more time to the learning process. After that, I got inspired by a friend of mine to continue my learning with Django, and its related technologies. 
And after that, here I am. I don't have any kind of experience in the programming professional world, but at this time, I'm firmly committed to learning more and more about coding, and to endeavour to raise my skills as much as I can. I am very much looking forward to join the programming professional world, because I know that the time here will greatly increase the learning process. 


## About this code

I've created a Makefile, where I added the most common commands that I've been using. There, you will be able to see that there is a command named `setup`. You will need to use it if is the first time that you run this project.
If you'd rather work terminal, just use next instructions:

> docker-compose build

> docker-compose run eventbrite python manage.py migrate

> docker-compose run eventbrite python manage.py loaddata backend/events/fixtures/*


This should be enough. Keep in mind that when you have dependencies issues, you can run: 
> sudo chown `whoami` -R .


## Part 1 - Creating the backend

* **Models:** This project has 3 different models: Event, Ticket, and Location.
* **Serializers:** Regarding serializers, I decided to create one for each model that will have an endpoint (ticket and event).
* **Views:** I also created two views. The first one will allow to show all the events in the DB. The second one is being used for showing all tickets belonging to a specific event.
* **URLs:** For the urls, I decided to use nested urls to help me relate all the tickets with their corresponding event.


## Part 2 - File Ingestion

 I've created 3 different JSON files that contains data from the 3 models. These data can be loaded to the API DB by using `Make loaddata`, or by the following command in the console:
> docker-compose run eventbrite python manage.py loaddata backend/events/fixtures/*

Also, there is a way that you can empty this DB in case you need to:
> docker-compose run api python manage.py flush



## Part 3 - Creating the Frontend

There is not a specific command to build the frontend, there is a file called package.json that contains all dependencies 
needed to create this API. When the dockerfile existing in the 'frontend' folder is built, the command 'npm install' will 
install all these dependencies in the docker image, so there's no need of doing it manually. 

For the Frontend, I decided to use Vue and Vue-Bootstrap. There's a landing page called 'EventsList.vue', where all events 
from the DB are shown to the user. From these events it's possible to see it respective thumbnail, location, and event name. When clicked, 
this images will redirect the user to 'EventDetail.vue'. Here it is shown the respective event name, location, description,
starting date, online label (if the event is online), and a 'Buy Ticket' button, which will redirect the user to 'TicketDetail.vue'. 
All tickets belonging to the clicked event are shown in this page (in case that that event has available tickets). The user 
will be able to select all the tickets they want, and that will trigger one alarm, showing that the ticket has been added 
to a hypothetical cart.

Along all this travelling between pages, the user will always be cared by a top header where, in this case, they will have 
the brand logo that redirects the user to the main page.


## Part 4 - Running the code
To run this code it is enough to use:
> docker-compose up

After that, you can simply check that everything works perfectly by checking the following links:

(For Django-Rest-Framework view)

http://0.0.0.0:8000/events/  
http://0.0.0.0:8000/events/2/  
http://0.0.0.0:8000/events/2/tickets/  



(For Frontend view)

http://localhost:8080/


(Keep in mind that the integer value can be switched for another one)