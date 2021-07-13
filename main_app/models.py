from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User



AMENITIES = (
    ('RST', 'Restroom'),
    ('BEN', 'Benches'),
    ('PIC', 'Picnic Tables'),
    ('VIS', 'Visitor Center'),
    ('DOG', 'Dog Friendly'),
    ('PLY', 'Playground'),
    ('WTR', 'Water Fountains'),
    ('BBQ', 'Barbeque Pit'),
    ('MTN', 'Mountain Biking'),
    ('RNG', 'Running'),
    ('HIK', 'Hiking'),
    ('SWM', 'Swimming'),
    ('PTH', 'Nature Path'),
    ('CMP', 'Camping'),
    ('BRD', 'Bird Watching'),
    ('BGN', 'Begginer'),
    ('INT', 'Intermediate'),
    ('ADV', 'Advanced')
)


class Amenity(models.Model):
    name = models.CharField(
        max_length=3,
        choices=AMENITIES,
        default=AMENITIES[0][0]
    )
    def __str__(self):
        return self.get_name_display()

# Create your models here.
class Trail(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(max_length=250)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    trail_length = models.DecimalField(max_digits=4, decimal_places=2, default= 00.00)
    

    def get_absolute_url(self):
        return reverse('detail', kwargs={'trail_id': self.id})
 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amenities = models.ManyToManyField(Amenity)

class Comment(models.Model):
    date = models.DateField('Comment Date')
    description = models.TextField(max_length=250)

    trail = models.ForeignKey(Trail, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'trail_id': self.trail_id})

    def __str__(self):
        return f"comment from {self.trail} on {self.date}"

    
    class Meta:
        ordering = ['-date']




# class Photo(models.Model):
#     url = models.CharField(max_length=200)

#     trail = models.ForeignKey(Trail, on_delete=models.CASCADE)