from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from backend.events.models import Event, Ticket
from backend.events.serializers import EventSimpleSerializer, EventSerializer, TicketSimpleSerializer, TicketSerializer


class EventViewSet(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Event.objects.all()
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ["name", "location", "description"]
    ordering = ("id",)

    def get_serializer_class(self):
        if self.action == "list":
            return EventSimpleSerializer
        else:
            return EventSerializer


class TicketViewSet(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Ticket.objects.all()
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ["name"]
    ordering = ("id",)

    def get_serializer_class(self):
        if self.action == "list":
            return TicketSimpleSerializer
        else:
            return TicketSerializer
