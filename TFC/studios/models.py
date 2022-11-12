from django.db import models

# Create your models here.
from django.db.models import ForeignKey


# class StudioManager(models.manager):
#     def create_studio(self):
#         pass


class Studio(models.Model):
    # name, address, geographical location, postal code, phone number, and a set of images
    # objects = StudioManager()
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    geographical_location = models.CharField(max_length=200)
    # Canada postal codes have 6 digits
    postal_code = models.CharField(max_length=6)
    # 10 digits so user knows to only input numbers
    phone_number = models.CharField(max_length=10)


class Image(models.Model):
    name = models.CharField()
    studio = ForeignKey(Studio, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='studio_images/')
    default = models.BooleanField(default=False)




