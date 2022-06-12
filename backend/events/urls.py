from rest_framework import routers
from django.urls import path, include

from backend.events.views import EventViewSet, TicketViewSet

app_name = "events"

router = routers.SimpleRouter()

router.register(r"events", EventViewSet, basename="events")
router.register(r"tickets", TicketViewSet, basename="tickets")

urlpatterns = [
    path('', include(router.urls)),
]
