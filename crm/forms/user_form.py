#!/usr/bin/env python
# -*- coding:utf8 -*-

from django import forms
from crm import models
from django.core.exceptions import ValidationError
from crm.forms.base_form import BootstrapModelForm

class UserInfoModelForm(BootstrapModelForm):
    confirm_password = forms.CharField(
        label='确认密码',
        widget=forms.PasswordInput(attrs={'placeholder':'确认密码'}),
    )
    class Meta:
        model = models.UserInfo
        labels = {'username':'用户名','password':'密码','email':'邮箱'}
        fields = ['username','password','confirm_password','email','phone','gender','depart']
        widgets = {
            'username':forms.TextInput(attrs={'placeholder':'用户名'},),
            'password':forms.PasswordInput(attrs={'placeholder':'密码'},),
            'email':forms.EmailInput(attrs={'placeholder':'邮箱'}),
            'phone':forms.TextInput(attrs={'placeholder':'手机号'}),
            'gender':forms.Select(attrs={'placeholder':'性别'}),
            'depart':forms.Select(attrs={'placeholder':'部门'})
        }
        # error_messages = {
        #     'username':{
        #         'required':'用户名不能为空',
        #     },
        #     'password':{
        #         'required':'密码不能为空',
        #     },
        #     'email':{
        #         'invalid':'邮箱格式不对',
        #     },
        #     'phone':{
        #         'required': '手机号不能为空',
        #     },
        #     'gender':{
        #         'required': '性别不能为空',
        #     },
        #     'depart':{
        #         'required': '所在部门不能为空',
        #     }
        # }

    def clean_confirm_password(self):
        pwd1 = self.cleaned_data['password']
        pwd2 = self.cleaned_data['confirm_password']
        if pwd1 != pwd2:
            raise ValidationError('两次密码不一致')
        return pwd2