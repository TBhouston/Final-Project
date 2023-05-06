


# Create your models here.

from django.db import models
import datetime

class Menu(models.Model):
    name = models.CharField(max_length=255, default="product name")
    description = models.TextField(default="product description")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    

    def __str__(self):
        return f'{self.name} - {self.price}'
    
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField(auto_now=False,null=True)

    def __str__(self):
        return f'{self.name} - {self.no_of_guests} guests'


