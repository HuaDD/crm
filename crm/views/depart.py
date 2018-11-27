from crm import models
from utils.memory_revers import memory_url
from utils.pagers import Page_Info
from crm.forms.depart_form import DepartModelForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,HttpResponse,redirect,reverse

# Create your views here.

@login_required
def depart_list(request):
    """
    部门列表
    :param request: 
    :return: 
    """
    all_count = models.Derartment.objects.all().count()
    page_info = Page_Info(request.GET.get('page'), all_count, 10, reverse('crm:depart_list'), 11)
    depart_list = models.Derartment.objects.all()[page_info.start():page_info.end()]
    return render(request, 'depart_list.html', {'depart_list':depart_list,'page_info': page_info})


def depart_add(request):
    """
    添加部门
    :param request: 
    :return: 
    """
    form = DepartModelForm()
    if request.method == 'POST':
        form = DepartModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('crm:depart_list'))
    return render(request, 'change.html', {'form':form})

def depart_edit(request,nid):
    """
    添加部门
    :param request: 
    :return: 
    """
    depart_obj = models.Derartment.objects.filter(id=nid).first()
    form = DepartModelForm(instance=depart_obj)
    if request.method == 'POST':
        form = DepartModelForm(data=request.POST,instance=depart_obj)
        if form.is_valid():
            form.save()
            return redirect(memory_url(request, 'crm:depart_list'))
    return render(request,'change.html',{'form':form})


def depart_del(request):
    """
    删除
    :param request: 
    :param nid: 
    :return: 
    """
    nid = request.GET.get('id')

    models.Derartment.objects.filter(id=nid).delete()
    return HttpResponse('删除成功')


