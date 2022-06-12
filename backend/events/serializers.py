from rest_framework import serializers

from backend.events.models import Ticket, Event


class EventSerializer(serializers.ModelSerializer):
    tickets = serializers.SerializerMethodField()

    def get_tickets(self, object):
        return Ticket.objects.get(id=object.tickets.id).name

    class Meta:
        model = Event
        fields = [
            "id",
            "name",
            "location",
            "description",
            "start_date",
            "end_date",
            "image",
            "is_online",
            "tickets",
        ]


class EventSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            "id",
            "name",
            "is_online",
        ]


class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = [
            "id",
            "name",
            "price",
            "total_amount",
            "left_amount",
        ]


class TicketSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = [
            "id",
            "name",
            "price",
        ]