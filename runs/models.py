from django.conf import settings
from django.db import models

class Run(models.Model):
    distance_miles = models.FloatField()
    start_time = models.DateTimeField()

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.distance_miles} miles started at {self.start_time}'