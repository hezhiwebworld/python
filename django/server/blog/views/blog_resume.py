from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

from blog.models import Resume
from blog.models import Power

@csrf_exempt  # 去掉csrf保护
def resume(request):
    Resume_queryset = Resume.objects.all()  # 得到queryset 对象
    Power_queryset = Power.objects.all()  # 得到queryset 对象
    Resume_list = []

    for art in Resume_queryset:
        # print(art.title)
        # print(art.author)
        # print(art.create_date)
        # print(art.content)
        # print(art.reading_amount)
        temp = model_to_dict(art)  # 将一个queryset对象转化为  字典
        Resume_list.append(temp)
    print(Resume_list)
    return JsonResponse({'articleList': 1})

