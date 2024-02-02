from django.db import models

# Create your models here.
class Booking(models.Model):
    title = models.CharField(max_length = 255)
    guests =  models.IntegerField()
    date = models.DateTimeField()
    
    def __str__(self):
        return self.title + ': ' + str(self.guests) + ' Guests'

class Menu(models.Model):
    title = models.CharField(max_length = 255)
    price = models.DecimalField(decimal_places = 2, max_digits = 10)
    inventory = models.IntegerField()
    
    def __str__(self):
        return self.title