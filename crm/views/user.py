#!/usr/bin/env python
# -*- coding:utf8 -*-

from crm import models
from utils.pagers import Page_Info
from crm.forms.user_form import UserInfoModelForm
from django.shortcuts import render,reverse,redirect,HttpResponse
from django.contrib.auth.decorators import login_required


@login_required
def user_list(request):
    """
    用户列表
    :param request: 
    :return: 
    """
    all_count = models.UserInfo.objects.all().count()
    page_info = Page_Info(request.GET.get('page'), all_count, 10, reverse('crm:user_list'), 11)
    user_list = models.UserInfo.objects.all()[page_info.start():page_info.end()]
    return render(request, 'user_list.html', {'user_list':user_list,'page_info':page_info})

def user_add(request):
    """
    添加用户
    :param request: 
    :return: 
    """
    form = UserInfoModelForm()
    if request.method == 'POST':
        form = UserInfoModelForm(data=request.POST)
        if form.is_valid():
            dic = form.cleaned_data
            models.UserInfo.objects.create_user(
                username=dic['username'],
                password=dic['password'],
                email=dic['email'],
                phone=dic['phone'],
                gender=dic['gender'],
                depart=dic['depart']
            )
            return redirect(reverse('crm:user_list'))
    return render(request, 'change.html', {'form':form})

def user_edit(request,nid):
    """
    添加用户
    :param request: 
    :return: 
    """
    user_obj = models.UserInfo.objects.filter(id=nid).first()
    form = UserInfoModelForm(instance=user_obj)
    if request.method == 'POST':
        form = UserInfoModelForm(data=request.POST,instance=user_obj)
        if form.is_valid():
            dic = form.cleaned_data
            form.save()
            user_obj.set_password(dic['password'])
            user_obj.save()
            return redirect(reverse('crm:user_list'))
    return render(request, 'change.html', {'form':form})

def user_del(request):
    """
    删除
    :param request: 
    :param nid: 
    :return: 
    """
    nid = request.GET.get('id')
    models.UserInfo.objects.filter(id=nid).delete()
    return HttpResponse('删除成功')




