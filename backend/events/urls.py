from django.urls import path, include
from rest_framework_nested import routers

from backend.events.views import EventViewSet, TicketViewSet

app_name = "events"

router = routers.SimpleRouter()
router.register(r'events', EventViewSet, basename='events')

files_router = routers.NestedSimpleRouter(router, r"events", lookup='event')
files_router.register(r'tickets', TicketViewSet, basename='ticketevent')

router.register(r"tickets", TicketViewSet, basename="tickets")

urlpatterns = [
    path('', include(router.urls)),
    path('', include(files_router.urls)),
]
