from django.db import models
from .models import Organization

#model for schedule

class Schedule(models.Model):
    """docstring for Schedule"""
    monday = models.BooleanField()
    tuesday = models.BooleanField()
    wednesday = models.BooleanField()
    thursday = models.BooleanField()
    friday = models.BooleanField()
    saturday = models.BooleanField()
    sunday = models.BooleanField()
    work_start = models.TimeField()
    work_end = models.TimeField()

class ScheduleOrg(models.Model):
    """docstring for ScheduleOrg"""
    schedule = models.ForeignKey(Schedule)
    organizatoin = models.ForeignKey(Organization)