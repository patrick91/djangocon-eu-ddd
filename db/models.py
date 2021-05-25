from django.db import models


class Event(models.Model):
    id = models.UUIDField(primary_key=True)
    title = models.CharField(max_length=255)
    start_date = models.DateField()
