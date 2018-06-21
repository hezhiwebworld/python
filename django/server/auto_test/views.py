from django.shortcuts import render, HttpResponse


from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from auto_test.serializers import UserSerializer, GroupSerializer
# Create your views here.


# 测试app是否正常运行
def HelloWorld(request):
    return HttpResponse("hello world")


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer