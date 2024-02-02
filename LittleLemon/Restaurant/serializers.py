from rest_framework import serializers
from . import models

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Menu
        fields = ['id', 'title', 'price', 'inventory']
        extra_kwargs = {'price': {'min_value': 0}, 'inventory': {'min_value': 0}}

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Booking
        fields = '__all__'