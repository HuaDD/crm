#!/usr/bin/env python
# -*- coding:utf8 -*-
from crm import models
from utils.pagers import Page_Info
from crm.forms.host_form import HostModelForm
from utils.memory_revers import memory_url
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse,render,reverse,redirect

@login_required
def host_list(request):
    """
    主机列表
    :param request: 
    :return: 
    """
    all_count = models.Host.objects.all().count()
    page_info = Page_Info(request.GET.get('page'), all_count, 10, reverse('crm:host_list'), 11)
    host_list = models.Host.objects.all()[page_info.start():page_info.end()]
    return render(request,'host_list.html',{'host_list':host_list,'page_info':page_info})

def host_add(request):
    """
    添加主机
    :param request: 
    :return: 
    """
    form = HostModelForm()
    if request.method == 'POST':
        form = HostModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('crm:host_list'))
    return render(request,'change.html',{'form':form})

def host_edit(request,hid):
    """
    编辑主机
    :param request: 
    :return: 
    """
    host_obj = models.Host.objects.filter(id=hid).first()
    form = HostModelForm(instance=host_obj)
    if request.method == 'POST':
        form = HostModelForm(data=request.POST,instance=host_obj)
        if form.is_valid():
            form.save()
            return redirect(memory_url(request,'crm:host_list'))
    return render(request,'change.html',{'form':form})

def host_del(request):
    """
    删除主机
    :param request: 
    :return: 
    """
    nid = request.GET.get('id')
    models.Course.objects.filter(id=nid).delete()
    return HttpResponse('删除成功')















