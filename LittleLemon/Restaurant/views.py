from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from . import models, serializers
from rest_framework.decorators import api_view, permission_classes

# Create your views here.
def index(request):
    return render(request, 'index.html')

class MenuItemView(generics.ListCreateAPIView):
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = models.Booking.objects.all()
    serializer_class = serializers.BookingSerializer
    permission_classes = [permissions.IsAuthenticated] 