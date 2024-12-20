# weather/models.py 
from django.db import models
from django.contrib.auth.models import User

#class base function 
class WeatherQuery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.location} ({self.timestamp})"

