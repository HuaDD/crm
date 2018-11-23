#!/usr/bin/env python
# -*- coding:utf8 -*-

from crm import models
from django import forms
from crm.forms.base_form import BootstrapModelForm


class DepartModelForm(BootstrapModelForm):
    class Meta:
        model = models.Derartment
        fields = '__all__'
        # widgets = {
        #     'title':forms.TextInput(attrs={'class':'form-control','placeholder':'部门名称'}),
        # }
        # error_messages={
        #     'title':{'required':'部门名称不能为空'}
        # }
