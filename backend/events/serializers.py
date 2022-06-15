from rest_framework import serializers

from backend.events.models import Ticket, Event, Location


class EventSerializer(serializers.ModelSerializer):
    tickets_list = serializers.SerializerMethodField()
    location = serializers.SerializerMethodField()

    def get_tickets_list(self, object):
        tickets_list = []
        for ticket in object.tickets.all():
            tickets_list.append(ticket.name)
        return tickets_list

    def get_location(self, object):
        return Location.objects.get(id=object.location.id).name

    class Meta:
        model = Event
        fields = [
            "id",
            "name",
            "location",
            "description",
            "start_date",
            "end_date",
            "is_online",
            "tickets",
            "tickets_list",
            "get_image",
            "get_thumbnail",
        ]


class EventSimpleSerializer(serializers.ModelSerializer):
    location = serializers.SerializerMethodField()

    def get_location(self, object):
        return Location.objects.get(id=object.location.id).name

    class Meta:
        model = Event
        fields = [
            "id",
            "name",
            "get_image",
            "get_thumbnail",
            "is_online",
            "location",
        ]


class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = [
            "id",
            "name",
            "price",
            "currency",
            "total_amount",
            "left_amount",
            "is_available",
        ]
