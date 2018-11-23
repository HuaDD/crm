#!/usr/bin/env python
# -*- coding:utf8 -*-
import re
from django.template import Library
from django.conf import settings

register = Library()
@register.inclusion_tag('rbac/auto_menu.html')
def get_menu(request):
    menu_list = request.session.get(settings.RBAC_SESSION_MENU_KEY)
    for item in menu_list:
        url = '^%s$'%item['url']
        if re.match(url,request.path_info):
            item['class'] = 'active'
    return {
        'menu_list':menu_list,
    }

@register.filter
def has_button(request,alias_url):
    permission_dict = request.session.get(settings.RBAC_SESSION_PERMISSION_KEY)
    if alias_url in permission_dict:
        return True


