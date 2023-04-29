from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Menu
from rest_framework import generics, viewsets, permissions
from .serializers import UserSerializer,menuSerializer
from rest_framework.decorators import api_view


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class MenuItemView(generics.ListCreateAPIView):
    queryset = menuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    



