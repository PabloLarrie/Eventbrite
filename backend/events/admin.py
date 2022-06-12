from django.contrib import admin
from django.contrib.auth.models import Permission

from backend.events.models import Event, Ticket

admin.site.register(Event)
admin.site.register(Ticket)
admin.site.register(Permission)
