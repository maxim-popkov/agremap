from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Organization(models.Model):
    """docstring for Organization"""
    def __str__(self):
        return self.name
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=2048)
    city = models.CharField(max_length=64)
    adress = models.CharField(max_length=256)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], blank=True) # validators should be a list
    website = models.URLField(max_length=64)
    num_views = models.IntegerField(default=0)
    longitude = models.CharField(max_length=32)
    latitude = models.CharField(max_length=32)
    srid = models.IntegerField(default=0)
        