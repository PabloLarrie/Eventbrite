from django.contrib import admin
from django.contrib.auth.models import Permission

from backend.events.models import Event, Ticket, Location

admin.site.register(Event)
admin.site.register(Ticket)
admin.site.register(Location)
admin.site.register(Permission)

readonly_fields = 'admin_photo'
