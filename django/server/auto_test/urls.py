
#  系统模块
from django.urls import path, include
from rest_framework import routers


# 自定义模块
from auto_test import views

router = routers.DefaultRouter()

router.register('users', views.UserViewSet)
router.register('groups', views.GroupViewSet)


urlpatterns = [
     path('', include(router.urls)),
     path('test/', views.HelloWorld),
     path('testlist/', views.test_list),
]







