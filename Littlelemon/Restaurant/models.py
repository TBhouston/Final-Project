from django.db import models
from django.contrib.auth.models import User
from .serializers import UserSerializer, MenuItemSerializer

# Create your models here.

class User(models.Model):
    url = models.URLField (max_length=200)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    groups = models.CharField(max_length=255)

    def __str__(self):
        return self.user

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places =2)
    Inventory = models.IntegerField()

    def __str__(self):
        return f'{self.title} : {self.price}'
    
    
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField(auto_now_add=False,null =True)
    
    def __str__(self):
        return self.name
