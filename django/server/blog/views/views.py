from django.shortcuts import render, HttpResponse

# Create your views here.

from django.views.generic import ListView


# 采取前后端分离的方式 不需要视图
class ArticleListView(ListView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello World!')
    
