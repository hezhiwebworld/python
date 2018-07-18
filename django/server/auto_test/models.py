#coding=utf-8
from django.db import models
from django.utils.timezone import now

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=50,unique=True)
    author = models.CharField(max_length=10)
    create_date =  models.DateTimeField(default=now) # 日期
    content = models.TextField()    # 文本
    reading_amount = models.IntegerField() #整数

    class Meta: #添加一个内嵌类。 不是必选参数
        ordering = ('create_date',) #设置默认排序方式

    def __str__(self):
        return self.title