#!/usr/bin/env python
# -*- coding:utf8 -*-
from django.http import QueryDict
from django.urls import reverse
from django.template import Library

register = Library()

@register.simple_tag
def memory_url(request,alias_url,*args,**kwargs):
    base_url = reverse(alias_url,args=args,kwargs=kwargs)
    if not request.GET:
        return base_url
    new_query_dict = QueryDict(mutable=True)
    new_query_dict['filter'] = request.GET.urlencode()
    url = '%s?%s' %(base_url,new_query_dict.urlencode())
    return url