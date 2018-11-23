from django.db import models

# Create your models here.
class Permissions(models.Model):
    """
    权限表
    """
    title = models.CharField(verbose_name='描述信息',max_length=64)
    url = models.CharField(verbose_name='URL',max_length=256)
    alias_url = models.CharField(verbose_name='URL别名',max_length=64,unique=True)
    icon = models.CharField(verbose_name='图标',max_length=64,null=True)
    is_menu = models.BooleanField(verbose_name='是否是菜单')

    def __str__(self):
        return self.title



class Role(models.Model):
    """
    角色表
    """
    title = models.CharField(verbose_name='角色',max_length=64)
    permission = models.ManyToManyField(to='Permissions',verbose_name='拥有的权限')

    def __str__(self):
        return self.title

class UserInfo(models.Model):
    """
    RBAC的用户表
    """
    # username = models.CharField(verbose_name='用户名',max_length=64)
    # password = models.CharField(verbose_name='密码',max_length=64)
    role = models.ManyToManyField(to=Role,verbose_name='对应角色')

    class Meta:
        abstract = True  # 表示在数据库迁移时不会生成相关的表

