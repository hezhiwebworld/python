#coding=utf-8
from django.db import models

import django.utils.timezone as timezone

# Create your models here.

# 数据模型

class NavTitle(models.Model):
    title = models.CharField(max_length=10,unique=True)

    def __str__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=50,unique=True)
    author = models.CharField(max_length=10)
    create_date =  models.DateTimeField(default=timezone.now()) # 日期
    content = models.TextField()    # 文本
    reading_amount = models.IntegerField() #整数

    # def __str__(self):
    #     return self.title

class Power(models.Model):
    powername = models.CharField(max_length=50,unique=True)
    create_date =  models.DateTimeField(default=timezone.now()) # 日期
    def __str__(self):
        return self.powername  

class Resume(models.Model):
    name = models.CharField(max_length=10,unique=True)
    age = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    worker = models.CharField(max_length=50)
    ownersite = models.CharField(max_length=20, unique=True)
    powername = models.ManyToManyField(Power)

    def __str__(self):
        return self.name  + '  ' + self.age  + '  ' + self.description  + '  ' + self.worker  + '  ' + self.ownersite 

class Site(models.Model):
    githubUrl = models.URLField(max_length=50)
    powerstack = models.TextField(max_length=1500)

    def __str__(self):
        return self.powerstack


    