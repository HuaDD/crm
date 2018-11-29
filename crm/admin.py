from django.contrib import admin
from crm import models

# Register your models here.
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['username','email','phone']


admin.site.register(models.UserInfo,UserInfoAdmin)