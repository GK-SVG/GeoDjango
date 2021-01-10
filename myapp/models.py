from django.db import models

# Create your models here.
class Measurement(models.Model):
    location = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    distance = models.DecimalField(decimal_places=2,max_digits=10)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.location} to {self.destination} distance {self.distance}' 
    