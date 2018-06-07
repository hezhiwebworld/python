


from django.http import JsonResponse
# from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
import json

# 导入自定义模块
from blog.models import NavTitle



@csrf_exempt # 去掉csrf保护
def nav_title(request):
    # request
    print('request')
    dct = {
        'fake' : 'test',
        'GET' : request.GET,
        'POST' : request.POST,
        'body' : request.body
    }

    NavTitle_list = []
    NavTitle_queryset = NavTitle.objects.all()  # 得到queryset 对象
    # print(NavTitle_queryset.values_list())
    for list in NavTitle_queryset:
        print(list.title)
        print(type(list) )
        NavTitle_list.append(list.title)

    #NavTitle_list = model_to_dict(NavTitle_queryset)
    
    print(NavTitle_list)

    # 在Django的实现中，request.POST对象是用于存储包含表单数据的对象，而在request.body中则包含了content中的原始(raw)非表单数据
    # 请求头类型为 Content-Type: application/x-www-form-urlencoded   request.POST对象
    # 请求头类型 Content-Type: application/json request.body中则包含了content中的原始(raw)非表单数据
    # return JsonResponse(json.dumps({'nav': NavTitle_list}, ensure_ascii=False), safe=False) 
    return JsonResponse({'nav': NavTitle_list})
    
