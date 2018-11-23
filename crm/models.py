from django.db import models
from django.contrib.auth.models import AbstractUser
from rbac.models import UserInfo as RbacUserInfo


# Create your models here.

class Derartment(models.Model):
    """
    部门表
    """
    title = models.CharField(verbose_name='部门名称', max_length=64)

    def __str__(self):
        return self.title


class UserInfo(AbstractUser,RbacUserInfo):
    """
    老师或者用户表
    """
    phone = models.CharField(verbose_name='手机号', max_length=11)
    gender_choice = (
        (1,'男'),
        (2,'女')
    )
    gender = models.IntegerField(verbose_name='性别',choices=gender_choice,null=True)
    depart = models.ForeignKey(verbose_name='部门', to='Derartment',null=True)

    def __str__(self):
        return self.username


class Course(models.Model):
    """
    课程表
    """
    title = models.CharField(verbose_name='课程名称', max_length=64)

    def __str__(self):
        return self.title


class ClassList(models.Model):
    """
    班级表
    """
    course = models.ForeignKey(verbose_name='课程名', to='Course')
    stage = models.CharField(verbose_name='期',max_length=16)
    teachers = models.ManyToManyField(verbose_name='老师', to='UserInfo')

    def __str__(self):
        return self.course

class Host(models.Model):
    """
    主机列表
    """
    hostname = models.CharField(verbose_name='主机名',max_length=64)
    hostpwd = models.CharField(verbose_name='主机密码',max_length=64)
    hostaddr = models.CharField(verbose_name='主机地址',max_length=64)
    business = models.CharField(verbose_name='对应业务',max_length=64)


    def __str__(self):
        return self.hostname

