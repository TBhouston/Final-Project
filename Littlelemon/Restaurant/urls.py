
from django.urls import path
from .views import BookingList, UserList, MenuList
from rest_framework import routers

urlpatterns = [
    path('bookings/', BookingList.as_view(), name='booking-list'),
    path('users/', UserList.as_view(), name='user-list'),
    path('menu/', MenuList.as_view(), name='menu-list'),
]
router = routers.DefaultRouter