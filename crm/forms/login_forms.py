#!/usr/bin/env python
# -*- coding:utf8 -*-
from django.contrib import auth
from django import forms
from crm import models
from django.forms import widgets
from django.core.exceptions import ValidationError


class LoginForms(forms.Form):
    username = forms.CharField(
        max_length=64,
        label='用户名',
        widget=widgets.TextInput(attrs={'class': 'form-control', 'placeholder': '用户名', }),
        error_messages={
            'required': '用户名不能为空',
        }
    )

    password = forms.CharField(
        max_length=16,
        label='密码',
        widget=widgets.PasswordInput(attrs={'class': 'form-control', 'placeholder': '密码'}),
        error_messages={
            'required': '密码不能为空',
        }
    )

    # def clean_username(self):
    #     username = self.cleaned_data.get('username')
    #     user = models.UserInfo.objects.filter(username=username).first()
    #     if user != username:
    #         raise ValidationError('用户名不存在')
    #     return username

    def clean_password(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = models.UserInfo.objects.filter(username=username).first()
        if not user.check_password(password):
            raise ValidationError('密码错误')
        return password

