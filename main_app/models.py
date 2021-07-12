from django.db import models

# Create your models here.
class Trail(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(max_length=250)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    trail_length = models.DecimalField(max_digits=4, decimal_places=2, default= 00.00)
    
    trail_length
    