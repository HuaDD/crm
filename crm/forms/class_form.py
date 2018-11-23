#!/usr/bin/env python
# -*- coding:utf8 -*-
from crm import models
from django import forms
from crm.forms.base_form import BootstrapModelForm

class ClassModelForm(BootstrapModelForm):
    class Meta:
        model = models.ClassList
        fields = '__all__'
        # widgets = {
        #     'stage':forms.TextInput(attrs={'class':'form-control','placeholder':'如:python全栈15期，就写15'}),
        #     'course':forms.Select(attrs={'class':'form-control','placeholder':'课程名称'}),
        #     'teachers':forms.SelectMultiple(attrs={'class':'form-control','placeholder':'老师名称'})
        # }

