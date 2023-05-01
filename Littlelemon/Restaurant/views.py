from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import MenuItem
from rest_framework import response
from rest_framework import generics, viewsets, permissions
from .serializers import MenuItemSerializer, SingleMenuItemSerializer, UserSerializer



# Create your views here.


@api_view ()
@permission_classes([IsAuthenticated])
#@authentication_classes([TokenAuthentication])

def msg(request):
    return Response({"message":"This view is protected"})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]



class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    



