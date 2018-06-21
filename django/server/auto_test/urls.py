
from django.urls import path


from auto_test import views


urlpatterns = [
     path('test/', views.HelloWorld),
]
