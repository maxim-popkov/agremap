from django.db import models
from .models import Organization

#model for service

class Service(models.Model):
    """docstring for Service"""
    def __str__(self):
        return self.name
    name = models.CharField(max_length=32)
    category = models.CharField(max_length=32)

class ServiceOrg(models.Model):
    """docstring for ServiceOrg"""
    service = models.ForeignKey(Service)
    organization = models.ForeignKey(Organization)
        