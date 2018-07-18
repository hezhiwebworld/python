
#coding=utf-8
from django.db import models

from django.utils.timezone import now

# Create your models here.

class OAuthUser(models.Model):
    author = models.CharField(max_length=50,verbose_name='用户')
    nickName = models.CharField(max_length=50, verbose_name='昵称')
    openid = models.CharField(max_length=50, verbose_name='用户')

    token = models.CharField(max_length=50,verbose_name='令牌')
    created_time = models.DateTimeField(default=now,verbose_name='创建时间')
    last_mod_time = models.DateTimeField(default=now, verbose_name='修改时间')

    def __str__(self):
        return self.nickName