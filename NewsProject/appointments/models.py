from django.db import models
from datetime import datetime
from django.utils.timezone import now

class Appointment(models.Model):
    date = models.DateField(
        default=now,
    )
    client_name = models.CharField(
        max_length=200
    )
    message = models.TextField()

    def __str__(self):
        return f'{self.client_name}: {self.message}'