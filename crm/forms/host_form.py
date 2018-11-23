#!/usr/bin/env python
# -*- coding:utf8 -*-
from crm import models
from crm.forms.base_form import BootstrapModelForm

class HostModelForm(BootstrapModelForm):

    class Meta:
        model = models.Host
        fields = '__all__'



