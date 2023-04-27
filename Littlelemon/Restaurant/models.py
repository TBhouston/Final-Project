from django.db import models
import datetime

# Create your models here.

class User(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    
    def __str__(self):
        return self.name



class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    bookingdate = models.DateTimeField (auto_now_add=False, null=True)

    def __str__(self):
        return self.name

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places =2)
    Inventory = models.IntegerField()

    def __str__(self):
        return self.title