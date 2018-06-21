from django.shortcuts import render, HttpResponse 

from django.http import JsonResponse

from django.contrib.auth.models import User, Group 
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view


from auto_test.serializers import UserSerializer, GroupSerializer, ArticleSerializer
# Create your views here.

# 自定义模块
from  auto_test.models import Article




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



@csrf_exempt
def test_list(request):
    if request.method == "GET":

        testList = Article.objects.all()
        testListSerializer = ArticleSerializer(testList, many=True) # 这里的many 疑问
        return JsonResponse(testListSerializer.data, safe=False)
    elif request.method == "POST":

        data  = JSONParser().parse(request)
        POSTSerializer = ArticleSerializer(data=data)

        if(POSTSerializer.is_valid()):
            POSTSerializer.save()
            return JsonResponse(POSTSerializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET'])
def test_apiview(request):
    return HttpResponse("测试apiView")