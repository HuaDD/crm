#!/usr/bin/env python
# -*- coding:utf8 -*-

from crm import models
from utils.pagers import Page_Info
from crm.forms.class_form import ClassModelForm
from utils.memory_revers import memory_url
from django.shortcuts import render,redirect,reverse,HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def class_list(request):
    """
    班级列表
    :param request: 
    :return: 
    """
    all_count = models.ClassList.objects.all().count()

    page_info = Page_Info(request.GET.get('page'), all_count, 10, reverse('crm:class_list'), 11)
    class_list = models.ClassList.objects.all()[page_info.start():page_info.end()]
    return render(request,'class_list.html',{'class_list':class_list,'page_info': page_info})

def class_add(request):
    """
    添加班级
    :param request: 
    :return: 
    """
    form = ClassModelForm()
    if request.method == "POST":
        form = ClassModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('crm:class_list'))

    return render(request, 'change.html', {'form':form})

def class_edit(request,nid):
    """
    编辑班级
    :param request: 
    :return: 
    """
    class_obj = models.ClassList.objects.filter(id=nid).first()
    form = ClassModelForm(instance=class_obj)
    if request.method == "POST":
        form = ClassModelForm(data=request.POST,instance=class_obj)
        if form.is_valid():
            form.save()
            return redirect(memory_url(request,'crm:class_list'))

    return render(request,'change.html',{'form':form})

def class_del(request):
    """
    删除
    :param request: 
    :return: 
    """
    nid = request.GET.get('id')
    models.ClassList.objects.filter(id=nid).delete()
    return HttpResponse('删除成功')



