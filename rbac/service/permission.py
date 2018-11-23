#!/usr/bin/env python
# -*- coding:utf8 -*-
from django.conf import settings

def init_permission(user_obj,request):
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
        'permission__is_menu',
        'permission__icon',

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
        if item['permission__is_menu']:
            menu_list.append({
                'alias_url':item['permission__alias_url'],
                'url':item['permission__url'],
                'title':item['permission__title'],
                'icon':item['permission__icon'],
            })
        permission_dict.setdefault(item['permission__alias_url'], {'url': item['permission__url']})
    # 放到session里面，在settings中配置session的key
    request.session[settings.RBAC_SESSION_PERMISSION_KEY] = permission_dict
    request.session[settings.RBAC_SESSION_MENU_KEY] = menu_list