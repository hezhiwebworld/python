from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

from blog.models import Resume
# from blog.models import Power



@csrf_exempt  # 去掉csrf保护
def resume(request):
    # 实体
    Resume_queryset = Resume.objects.get(name="何志")  # 得到queryset 对象
    Power_queryset = Resume_queryset.powername.values_list('powername',flat=True)  # 得到queryset 对象
    # value()
    print(Power_queryset)
    Power_list = []
    # print(Power_queryset)
    for art in Power_queryset:
        Power_list.append(art)

    temp = model_to_dict(Resume_queryset)  # 将一个queryset对象转化为  字典
    # power_dict = model_to_dict(Power_queryset)
    # Resume_list.append(temp)
    print(type(Power_list[0]))
    # print(power_dict)
    print(Power_list)
    # print(temp.name)
    # for key in temp:
    #     print(temp.key)
    temp['powername'] = Power_list
    del temp['id']

    returnObject = {
        'returnCode': 0,
        'returnMsg' : "成功" ,
        'articleList':temp
    }
    return JsonResponse(returnObject, safe=False)

