from django.db import models
from django.core.validators import RegexValidator

#model for metropoliten
class Metropoliten(models.Model):
    """docstring for Metropoliten"""
    city = models.CharField(max_length=64)
    station = models.CharField(max_length=32)

    def __str__(self):
        return self.station


# model for Organization.
class Organization(models.Model):
    """docstring for Organization"""
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    
    city = models.CharField(max_length=64)
    address = models.CharField(max_length=256)
    metropolitens = models.ManyToManyField(Metropoliten)
    
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(max_length=64, validators=[phone_regex], blank=True) # validators should be a list
    
    website = models.URLField(max_length=64, blank=True)
    
    ava_image = models.ImageField(upload_to='uploads/', null=True)

    longitude = models.CharField(max_length=32, default='-1')
    latitude = models.CharField(max_length=32, default='-1')
    srid = models.IntegerField(default=0)
    
    num_views = models.IntegerField(default=0)
    is_deleted = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    email_approve = models.EmailField()

    # def get_absolute_url(self):
    #     from django.core.urlresolvers import reverse
    #     return reverse('agreapp.views.detail_view', args=[str(self.id)])

    def __str__(self):
        return self.name


class OrganizationRequest(models.Model):
    """docstring for Organization"""
    # required in form fields
    name = models.CharField(max_length=128, blank=False)
    city = models.CharField(max_length=64, blank=False)
    address = models.CharField(max_length=256, blank=False)
    email_approve = models.EmailField(blank=False)
    
    metropoliten = models.CharField(max_length=32, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(max_length=64, validators=[phone_regex], blank=True) # validators should be a list
    website = models.URLField(max_length=64, blank=True)
    description = models.TextField(max_length=2048, blank=True)
    
    is_deleted = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)

    related_org = models.OneToOneField(Organization, blank=True, null=True)



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
