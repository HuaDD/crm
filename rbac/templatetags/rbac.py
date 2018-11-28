#!/usr/bin/env python
# -*- coding:utf8 -*-
import re
from django.template import Library
from django.conf import settings

register = Library()
@register.inclusion_tag('rbac/auto_menu.html')
def get_menu(request):
    """
    自动生成菜单
    :param request: 
    :return: 
    """
    """
    menu_list = 
        [
            {
                'id': 1, 
                'title': '信息列表', 
                'icon': 'fa-pencil-square', 
                'children': 
                    [
                        {
                            'title': '部门列表', 
                            'alias_url': 'depart_list', 
                            'url': '/crm/depart/list/'}, 
                            
                        {
                            'title': '用户列表', 
                            'alias_url': 'user_list', 
                            'url': '/crm/user/list/'
                        }
                    ]
            }
        ]
    
    """
    menu_list = request.session.get(settings.RBAC_SESSION_MENU_KEY)
    for item in menu_list:
        for child in item['children']:
            if child['alias_url'] == getattr(request,settings.RBAC_CURRENT_PARENT_KEY,None):
                child['class'] = 'active'
                item['class'] = ''
    return {'menu_list':menu_list,}

@register.filter
def has_button(request,alias_url):
    permission_dict = request.session.get(settings.RBAC_SESSION_PERMISSION_KEY)
    if alias_url in permission_dict:
        return True

@register.inclusion_tag('rbac/record.html')
def get_record(request):
    record_list = getattr(request,settings.RBAC_RBCORD_LIST)
    return {'record_list':record_list}