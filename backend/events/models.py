from PIL import Image
from django.db import models
from io import BytesIO
from django.core.files import File


class Location(models.Model):
    name = models.CharField(max_length=40)


class Ticket(models.Model):
    name = models.CharField(max_length=40)
    price = models.PositiveIntegerField()
    total_amount = models.PositiveIntegerField()
    left_amount = models.PositiveIntegerField()
    currency = models.CharField(max_length=3, blank=True)

    def is_available(self):
        return bool(self.left_amount)


class Event(models.Model):
    name = models.CharField(max_length=50, unique=True)
    location = models.ForeignKey("events.Location", related_name="location_events", on_delete=models.CASCADE, null=True)
    description = models.TextField(max_length=700)
    start_date = models.DateField()
    end_date = models.DateField()
    is_online = models.BooleanField(default=False)
    tickets = models.ManyToManyField("events.Ticket", related_name="events", blank=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)

    class Meta:
        ordering = ('-start_date',)

    def __str__(self):
        return self.name

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail
