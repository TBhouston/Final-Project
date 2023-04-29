from django.contrib import admin
from django.apps import apps
from .models import Booking, Menu

# Register your models here.
admin.site.register (Booking)
admin.site.register(Menu)