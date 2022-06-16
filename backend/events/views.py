from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from backend.events.models import Event, Ticket
from backend.events.serializers import EventSerializer, TicketSerializer


class EventViewSet(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Event.objects.all()
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ["name", "location", "description"]
    ordering = ("id",)

    def get_serializer_class(self):
        return EventSerializer


class TicketViewSet(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ["name"]
    ordering = ("id",)

    def get_queryset(self):
        return Ticket.objects.filter(events=self.kwargs['event_pk'])

    def get_serializer_class(self):
        return TicketSerializer
