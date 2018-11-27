#!/usr/bin/env python
# -*- coding:utf8 -*-
from django.urls import reverse

def memory_url(request,alias_url,*args,**kwargs):
    """
    反向生成url
    :param request: 
    :param alias_url: 
    :return: 
    """
    url = reverse(alias_url,args=args,kwargs=kwargs)
    filter = request.GET.get('filter')
    if not filter:
        return url
    return '%s?%s' %(url,filter)
