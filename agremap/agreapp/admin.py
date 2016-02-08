from django.contrib import admin
from .models import (Organization, OrganizationRequest,
                    Metropoliten, 
                    Service, ServiceOrg, 
                    Schedule, ScheduleOrg)

from django.apps import apps

#функция, которая отмечает организации как подтвержденные
def set_true_is_approve(modeladmin, request, queryset):
    orgs_approved = queryset.update(is_approved = True)
    if orgs_approved == 1:
        mess = "1 organization was"
    else:
        mess = "%s organizations were" % orgs_approved
    modeladmin.message_user(request, "%s  approved." % mess)
set_true_is_approve.short_description = "is_approved field set value 'True'"

#функция которая отмечает организации как НЕ подтвержденные
def set_false_is_approve(modeladmin, request, queryset):
    orgs_dis_approved = queryset.update(is_approved = False)
    if orgs_dis_approved == 1:
        mess = "1 organization was"
    else:
        mess = "%s organizations were" % orgs_dis_approved
    modeladmin.message_user(request, "%s dis approved." % mess)
set_false_is_approve.short_description = "is_approved field set value 'False'"

#Organization Admin Settings
class OrganizationRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'address', 'is_deleted', 
                    'is_approved', 'phone_number', 'website', 'metropoliten')

    actions = [set_true_is_approve, set_false_is_approve]

#Organization Admin Settings
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'address', 'is_deleted', 
                    'is_approved', 'num_views', 'phone_number', 'website')
    filter_horizontal = ('metropolitens',)

    actions = [set_true_is_approve, set_false_is_approve]


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
admin_registr = [(Organization, OrganizationAdmin),
                 (OrganizationRequest, OrganizationRequestAdmin)] # (Organization, OrganizationAdmin)
for model, model_admin in admin_registr:
    admin.site.register(model, model_admin)

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
