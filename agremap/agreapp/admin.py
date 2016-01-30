from django.contrib import admin
from .models import (Organization, 
                    Metropoliten, 
                    Service, ServiceOrg, 
                    Schedule, ScheduleOrg)

from django.apps import apps


#Organization Admin Settings
class OrganizationAdmin(admin.ModelAdmin):
    pass


#Metropoliten Admin Settings
class MetropolitenAdmin(admin.ModelAdmin):
    pass


# class MetropolitenOrgAdmin(admin.ModelAdmin):
#     pass


#Service Admin Settings
class ServiceAdmin(admin.ModelAdmin):
    pass


class ServiceOrgAdmin(admin.ModelAdmin):
    pass


#Schedule Admin Settings
class ScheduleAdmin(admin.ModelAdmin):
    pass


class ScheduleOrgAdmin(admin.ModelAdmin):
    pass



# Register your models here.
admin_registr = [] # (Organization, OrganizationAdmin)

# автомтаически регистрирует все модели из приложения
# если регистрируется новая модель со специальными настройками, её нужно отсюда исключить
admin_models = [m for m, a in admin_registr]
app_models = apps.get_app_config('agreapp').get_models()
for model in app_models:
    # print(model)
    if model not in admin_models:
        try:
            admin.site.register(model)
        except AlreadyRegistered:
            pass
