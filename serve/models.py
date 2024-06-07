from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=15)
    message = models.TextField()
    number = models.IntegerField()
    
    def __str__(self):
        return self.name 

class Car(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.CharField(max_length=255, default='images/default.png')

    def __str__(self):
        return self.name

class Booking(models.Model):
    car = models.CharField(max_length=100)
    quantity = models.IntegerField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.car