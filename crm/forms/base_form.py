#!/usr/bin/env python
# -*- coding:utf8 -*-
from django import forms


class BootstrapModelForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(BootstrapModelForm,self).__init__(*args,**kwargs)
        for k,v in self.fields.items():
            v.widget.attrs['class'] = 'form-control'