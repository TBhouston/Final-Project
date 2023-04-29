from django.contrib import admin
from django.urls import path, include
from . import views 
from rest_framework import routers
from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)




urlpatterns = [
    path('', include(router.urls)),  
    path('api-auth/', include("rest_framework.urls", namespace="rest_framework")),
    path('admin/', admin.site.urls),
    path ('menu/', views.MenuItemView.as_view()),
    path ('menu/<int:pk>/', views.SingleMenuItemView.as_view()),
]