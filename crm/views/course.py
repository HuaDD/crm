#!/usr/bin/env python
# -*- coding:utf8 -*-

from crm import models
from utils.pagers import Page_Info
from crm.forms.course_form import CourseModelForm
from utils.memory_revers import memory_url
from django.shortcuts import render,reverse,redirect,HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def course_list(request):
    """
    课程列表
    :param request: 
    :return: 
    """
    all_count = models.Course.objects.all().count()
    page_info = Page_Info(request.GET.get('page'), all_count, 10, reverse('crm:course_list'), 11)
    course_list = models.Course.objects.all()[page_info.start():page_info.end()]
    return render(request,'course_list.html',{'course_list':course_list,'page_info': page_info})

def course_add(request):
    """
    添加课程
    :param request: 
    :return: 
    """
    form = CourseModelForm()
    if request.method =="POST":
        form = CourseModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('crm:course_list'))
    return render(request, 'change.html', {'form':form})

def course_edit(request,nid):
    """
    添加课程
    :param request: 
    :return: 
    """
    course_obj = models.Course.objects.filter(id=nid).first()
    form = CourseModelForm(instance=course_obj)
    if request.method =="POST":
        form = CourseModelForm(data=request.POST,instance=course_obj)
        if form.is_valid():
            form.save()
            return redirect(memory_url(request,'crm:course_list'))
    return render(request,'change.html',{'form':form})


def course_del(request):
    """
    删除
    """
    nid = request.GET.get('id')
    models.Course.objects.filter(id=nid).delete()
    return HttpResponse('删除成功')

