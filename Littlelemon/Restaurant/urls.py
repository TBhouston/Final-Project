from django.contrib import admin
from django.urls import path, include
from . import views 
from rest_framework import routers
from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)    
router.register(r"menu", views.MenuViewSet)
router.register(r"tables", views.BookingViewSet)




urlpatterns = [
    path('', include(router.urls)),  
    path('api-auth/', include("rest_framework.urls", namespace="rest_framework")),
    path('admin/', admin.site.urls),
    path ('menu/', views.MenuItemView.as_view()),
    path ('menu/<int:pk>/', views.SingleMenuItemView.as_view()),
    path('menu-items/', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>/', views.SingleMenuItemsView.as_view()),
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token)

 
]