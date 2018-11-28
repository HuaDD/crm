#!/usr/bin/env python
# -*- coding:utf8 -*-
from collections import OrderedDict
from django.conf import settings

def init_permission(user_obj, request):
    """
    权限信息的初始化,将权限信息放到session中
    :param request: 
    :return: 
    """
    # 获取登录用户的所有权限信息
    permission_list = user_obj.role.filter(permission__title__isnull=False).values(
        'permission__title',
        'permission__alias_url',
        'permission__url',
        'permission__icon',
        'permission__menu_id',
        'permission__menu__title',
        'permission__menu__icon',
        'permission__parent__alias_url',

    ).distinct()
    """
     生成这样格式的数据
     {
    'depart_list': {'url': '/depart_list/'}, 
    'depart_add': {'url': '/depart/add/'}, 
    'depart_edit': {'url': '/depart/edit/(\\d+)'}, 
    'depart_del': {'url': '/depart/del/(\\d+)/'}
    }
    """
    permission_dict = {}
    menu_list = []
    for item in permission_list:
        if item['permission__menu_id']:
            menu_list.append({
                'alias_url': item['permission__alias_url'],
                'url': item['permission__url'],
                'title': item['permission__title'],
                'icon': item['permission__icon'],
                'menu_id': item['permission__menu_id'],
                'menu_title': item['permission__menu__title'],
                'menu_icon': item['permission__menu__icon'],

            })
        permission_dict.setdefault(item['permission__alias_url'], {'url': item['permission__url'],'parent':item['permission__parent__alias_url'],'title':item['permission__title']})
    menu_dict = OrderedDict()
    for item in menu_list:
        menu_id = item['menu_id']
        if menu_id in menu_dict:
            menu_dict[menu_id]['children'].append({
                'title': item['title'],
                'alias_url': item['alias_url'],
                'url': item['url']
            })
        else:
            menu_dict[menu_id] = {
                'id': menu_id,
                'title': item['menu_title'],
                'icon': item['menu_icon'],
                'class':'hide',
                'children': [
                    {
                        'title': item['title'],
                        'alias_url': item['alias_url'],
                        'url': item['url'],
                    }
                ]
            }
    """
    menu_dict = 
    {
	    1: {
            'id': 1, 
            'title': '信息列表', 
            'icon': 'fa-pencil-square', 
            'children': 
                [
                    {
                        'title': '部门列表', 
                        'alias_url': 'depart_list', 
                        'url': '/crm/depart/list/', 
                        'icon': 'fa-map-o'
                    }, 
                    {
                        'title': '用户列表', 
                        'alias_url': 
                        'user_list', 
                        'url': '/crm/user/list/'
                    }
                ]
            }
    }
    
    """
    # 放到session里面，在settings中配置session的key
    request.session[settings.RBAC_SESSION_PERMISSION_KEY] = permission_dict
    request.session[settings.RBAC_SESSION_MENU_KEY] = list(menu_dict.values())
