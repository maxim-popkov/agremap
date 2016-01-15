from django.db import models
from django.core.validators import RegexValidator

# model for Organization.
class Organization(models.Model):
    """docstring for Organization"""
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=2048)
    
    city = models.CharField(max_length=64)
    adress = models.CharField(max_length=256)
    
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(max_length=64, validators=[phone_regex], blank=True) # validators should be a list
    
    website = models.URLField(max_length=64)
    num_views = models.IntegerField(default=0)
    
    longitude = models.CharField(max_length=32)
    latitude = models.CharField(max_length=32)
    srid = models.IntegerField(default=0)
    
    is_deleted = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
        
    def __str__(self):
        return self.name


#model for schedule
class Schedule(models.Model):
    """docstring for Schedule"""
    monday = models.BooleanField(default=False)
    tuesday = models.BooleanField(default=False)
    wednesday = models.BooleanField(default=False)
    thursday = models.BooleanField(default=False)
    friday = models.BooleanField(default=False)
    saturday = models.BooleanField(default=False)
    sunday = models.BooleanField(default=False)

    work_start = models.TimeField()
    work_end = models.TimeField()


class ScheduleOrg(models.Model):
    """docstring for ScheduleOrg"""
    schedule = models.ForeignKey(Schedule)
    organization = models.ForeignKey(Organization)


#model for service
class Service(models.Model):
    """docstring for Service"""
    name = models.CharField(max_length=32)
    category = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class ServiceOrg(models.Model):
    """docstring for ServiceOrg"""
    service = models.ForeignKey(Service)
    organization = models.ForeignKey(Organization)


#model for metropoliten
class Metropoliten(models.Model):
    """docstring for Metropoliten"""
    city = models.CharField(max_length=64)
    station = models.CharField(max_length=32)

    def __str__(self):
        return self.station


class MetropolitenOrg(models.Model):
    """docstring for MetropolitenOrg"""
    metropoliten = models.ForeignKey(Metropoliten)
    organization = models.ForeignKey(Organization)
