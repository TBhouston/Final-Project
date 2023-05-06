
from django.urls import include, path
from .views import BookingList, UserList, MenuList
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from . import views

router=routers.DefaultRouter()
router.register('menu',views.MenuViewSet)
router.register('booking',views.BookingViewSet)
router.register('users',views.UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('bookings/', BookingList.as_view(), name='booking-list'),
    path('users/', UserList.as_view(), name='user-list'),
    path('menu/', MenuList.as_view(), name='menu-list'),
    path('menu-items/',views.SingleMenuItems.as_view()),
    path('menu-items/<int:pk>/',views.SingleMenuItems.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework_v1')),
    path('api-token-auth/', obtain_auth_token),
  
      ]
