from django.contrib import admin

from backend.events.models import Event, Ticket, Location

admin.site.register(Event)
admin.site.register(Ticket)
admin.site.register(Location)

readonly_fields = 'admin_photo'
