#!/usr/bin/env python
# -*- coding:utf8 -*-
from django.contrib import auth
from crm.forms.login_forms import LoginForms
from django.conf import settings
from django.shortcuts import render, reverse, redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from rbac.service.permission import init_permission


# @login_required
def index(request):
    return render(request, 'index.html')

def login(request):
    return_url = request.get_full_path()
    forms_obj = LoginForms()
    if request.method == 'POST':
        forms_obj = LoginForms(data=request.POST)
        if forms_obj.is_valid():
            dic = forms_obj.cleaned_data
            # 判断用户登录
            user = auth.authenticate(username=dic['username'], password=dic['password'])

            # 调用rbac中的权限信息初始化函数
            init_permission(user,request)
            permission_dict = request.session.get(settings.RBAC_SESSION_PERMISSION_KEY)
            if user:
                # 登录成功执行
                auth.login(request, user)
                if '=' in return_url:
                    return_url = return_url.split('=')
                    ret = redirect(return_url[1])
                else:
                    ret = redirect(reverse('crm:index'))
                return ret
    return render(request, 'login.html', {'forms_obj': forms_obj})

def current_user(request):
    username = request.user.username
    return HttpResponse(username)

def logout(request):
    auth.logout(request)
    return redirect(reverse('crm:login'))
