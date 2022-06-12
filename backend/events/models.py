from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver


class Event(models.Model):
    name = models.CharField(max_length=50, unique=True)
    location = models.CharField(max_length=60)
    description = models.TextField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    image = models.ImageField()
    is_online = models.BooleanField(default=False)
    tickets = models.ForeignKey("events.Ticket", related_name="events", on_delete=models.CASCADE, null=True)

    @receiver(post_delete, sender=image)
    def post_save_image(sender, instance, *args, **kwargs):
        try:
            instance.img.delete(save=False)
        except:
            pass


class Ticket(models.Model):
    name = models.CharField(max_length=40)
    price = models.PositiveIntegerField()
    total_amount = models.PositiveIntegerField()
    left_amount = models.PositiveIntegerField()

    def avaliable(self):
        return bool(self.left_amount)
