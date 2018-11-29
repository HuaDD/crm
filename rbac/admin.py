from django.contrib import admin
from rbac import models

# Register your models here.
class PermissionsAdmin(admin.ModelAdmin):
    list_display = ['title','alias_url','url','menu','parent']



admin.site.register(models.Permissions,PermissionsAdmin)


class RoleAdmin(admin.ModelAdmin):
    list_display = ['title']

admin.site.register(models.Role,RoleAdmin)


class MenuAdmin(admin.ModelAdmin):
    list_display = ['title','icon']

admin.site.register(models.Menu, MenuAdmin)