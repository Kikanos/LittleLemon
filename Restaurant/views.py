from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
#from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework.decorators import permission_classes

# Create your views here.
def index(request):
    return render(request, 'index.html', {})


class MenuItemView(ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.filter(id=1)
    serializer_class = MenuSerializer


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]


#class Bookingview(APIView):
#    def get(request):
#        items = Booking.objects.all()
#        serializer = BookingSerializer(items, many=True )
#        return Response (serializer.data)
    
#def Menuview(self, request):
#    serializer = menuSerializer(data=request.data)
#    if serializer.is_valid():
#        serializer.save()
#        return Response({"status" : "success"  , "data" : "serializer.data"})