#!/usr/bin/env python
# -*- coding:utf8 -*-
from django import forms
from crm import models
from crm.forms.base_form import BootstrapModelForm

class CourseModelForm(BootstrapModelForm):
    class Meta:
        model = models.Course
        fields = '__all__'
        # widgets = {
        #     'title':forms.TextInput(attrs={'class':'form-control','placeholder':'课程名称'}),
        # }
        #
        # error_messages={
        #     'title':{
        #         'required':'课程名不能为空'
        #     },
        # }