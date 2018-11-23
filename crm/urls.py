"""crm_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from crm.views import home,depart,user,course,class_list,host

urlpatterns = [
    url(r'^login/$', home.login,name='login'),
    url(r'^logout/$', home.logout,name='logout'),
    url(r'^index/$', home.index,name='index'),

    url(r'^depart/list/$', depart.depart_list,name='depart_list'),
    url(r'^depart/add/$', depart.depart_add,name='depart_add'),
    url(r'^depart/edit/(\d+)/$', depart.depart_edit,name='depart_edit'),
    url(r'^depart/del/$', depart.depart_del,name='depart_del'),

    url(r'^user/list/$', user.user_list,name='user_list'),
    url(r'^user/add/$', user.user_add,name='user_add'),
    url(r'^user/edit/(\d+)/$', user.user_edit,name='user_edit'),
    url(r'^user/del/$', user.user_del,name='user_del'),

    url(r'^course/list/$', course.course_list,name='course_list'),
    url(r'^course/add/$', course.course_add,name='course_add'),
    url(r'^course/edit/(\d+)/$', course.course_edit,name='course_edit'),
    url(r'^course/del/$', course.course_del,name='course_del'),

    url(r'^class/list/$', class_list.class_list,name='class_list'),
    url(r'^class/add/$', class_list.class_add,name='class_add'),
    url(r'^class/edit/(\d+)/$', class_list.class_edit,name='class_edit'),
    url(r'^class/del/$', class_list.class_del,name='class_del'),

    url(r'^current_user/$', home.current_user,name='current_user'),

    url(r'^host/list/$', host.host_list, name='host_list'),
    url(r'^host/add/$', host.host_add, name='host_add'),
    url(r'^host/edit/(\d+)/$', host.host_edit, name='host_edit'),
    url(r'^host/del/$', host.host_del, name='host_del'),


]
