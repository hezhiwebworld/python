from django.http import JsonResponse
from blog.models import Article
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict


@csrf_exempt # 去掉csrf保护
def blog_acticle_lsit(request):
    
    Article_queryset = Article.objects.all()  # 得到queryset 对象
    Article_list = []

    for art  in Article_queryset:
        # print(art.title)
        # print(art.author)
        # print(art.create_date)
        # print(art.content)
        # print(art.reading_amount)
        temp = model_to_dict(art)  # 将一个queryset对象转化为  字典
        Article_list.append(temp)
    print(Article_list)
    return JsonResponse({'articleList': Article_list})
    
