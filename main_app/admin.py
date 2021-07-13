from django.contrib import admin
from .models import Trail, Comment, Amenity

# Register your models here.
admin.site.register(Trail)
admin.site.register(Comment)
admin.site.register(Amenity)
