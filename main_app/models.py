from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Trail(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(max_length=250)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    trail_length = models.DecimalField(max_digits=4, decimal_places=2, default= 00.00)
 
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    date = models.DateField('Comment Date')
    description = models.TextField(max_length=250)

    trail = models.ForeignKey(Trail, on_delete=models.CASCADE)

    

# class Photo(models.Model):
#     url = models.CharField(max_length=200)

#     trail = models.ForeignKey(Trail, on_delete=models.CASCADE)