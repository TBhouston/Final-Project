

# Create your views here.
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Booking, Menu, User
from .serializers import bookingSerializer, menuSerializer, userSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

class BookingView(APIView):
    def get(self, request):
        items = Booking.objects.all()
        serializer = bookingSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = bookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("status": "success")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)