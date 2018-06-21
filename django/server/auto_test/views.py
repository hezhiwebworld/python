from django.shortcuts import render, HttpResponse

# Create your views here.



def HelloWorld(request):
    return HttpResponse("hello world")