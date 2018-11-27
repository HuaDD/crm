#!/usr/bin/env python
# -*- coding:utf8 -*-
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crm_demo.settings")
import django
django.setup()
from  crm import models

# class_list  = models.ClassList.objects.all()
# for i in class_list:
#     print(i)
#     for n in i.teachers.all():
#         print(n.username,n.phone)

# host = models.Host.objects.filter(id=1).first()
# print(host)

user_list = []
for i in range(1,50):
    user_list.append(models.Course(title='course%s' %i))
#
# models.Derartment.objects.bulk_create(user_list,10)
models.Course.objects.bulk_create(user_list,10)
# models.Derartment.objects.create(title='depart1')