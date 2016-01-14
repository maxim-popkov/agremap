from django.db import models
from .models import Organization

#model for metropoliten

class Metropoliten(models.Model):
    """docstring for Metropoliten"""
    def __str__(self):
        return self.station
    city = model.CharField(max_length=64)
    station = model.CharField(max_length=32)

class MetropolitenOrg(models.Model):
    """docstring for MetropolitenOrg"""
    metropoliten = models.ForeignKey(Metropoliten)
    organization = models.ForeignKey(Organization)