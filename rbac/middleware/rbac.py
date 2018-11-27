#!/usr/bin/env python
# -*- coding:utf8 -*-
import re
from django.conf import settings
from django.shortcuts import HttpResponse,redirect,reverse,render
from django.utils.deprecation import MiddlewareMixin

class RbacMiddleware(MiddlewareMixin):
    def process_request(self,request):
        """
        权限的校验
        :param request: 
        :return: 
        """
        # 1.处理白名单，在settings中设置
        for reg in settings.RBAC_VALID_LIST:
            if re.match(reg,request.path_info):
                return

        # 2.权限校验
        # 2.1 先去session中获取用户所有的权限信息
        permission_dict = request.session.get(settings.RBAC_SESSION_PERMISSION_KEY)
        # 2.2 判断用户的权限信息在没在session中，如果没有表示没登录，则跳转到登录页面
        if not permission_dict:
            return redirect(reverse('crm:login'))

        # 2.3 所有用户都可以访问的url列表
        for reg in settings.RBAC_NO_PERMISSION_LIST:
            if re.match(reg,request.path_info):
                return None

        # 2.4 获取当前用户请求的url地址,和session中的权限信息进行比对
        for name,url_info in permission_dict.items():
            url = '^%s$' % url_info['url']
            if re.match(url,request.path_info):
                return None

        return HttpResponse('您没有权限，无法执行此功能')


















