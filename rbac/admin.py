from django.contrib import admin
from rbac import models

# Register your models here.
admin.site.register(models.Permissions)
admin.site.register(models.Role)