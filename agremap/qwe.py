# coding: utf-8
from agreapp.models import Organization, Schedule, ScheduleOrg, Service, ServiceOrg, Metropoliten, MetropolitenOrg
from datetime import time
org = Organization(name='name1', description='desc1', city='city1', adress='adress1', phone_number='+74999999', website='www.ex1.ru', longitude='123', latitude='456')
org.save()
t1 = time(1,2,3,4)
t2 = time(5,6,7,8)
sche=Schedule(monday=True,tuesday=True,wednesday=True,thursday=True,friday=True,saturday=False,sunday=False,work_start=t1,work_end=t2)
sche.save()
scheo = ScheduleOrg(schedule=sche, organization=org)
scheo = ScheduleOrg.objects.create(schedule=sche, organization=org)