from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Booking
from .models import Menu

# Register your models here.
admin.site.register(Booking)
admin.site.register(Menu)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'no_of_guests', 'booking_datetime')

class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'inventory') 