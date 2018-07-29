from django.http import JsonResponse
from blog.models import Article
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict


@csrf_exempt # 去掉csrf保护
def blog_acticle_lsit(request):
    print(request.GET.get('page'))
    # page =  0;
    # if(request.GET.get('page')):
    #     page = request.GET.get('page')
    Article_list = []
    try:
        page = int(request.GET.get('page', 1))
        onePageCount =20
        Article_queryset = Article.objects.all() # 得到的是一个queryset

        totalCount = Article_queryset.count()
        print(totalCount)
        if(page -1 )* onePageCount >= totalCount:
            return  JsonResponse({'return': 'nodata'}, safe=False)
        else:
            start = ( page - 1) * onePageCount
            end = page*onePageCount
            if page*onePageCount > totalCount:
                for art in  Article_queryset[start:end]:
                    temp = model_to_dict(art)
                    Article_list.append(temp)
                return  JsonResponse(Article_list, safe=False)
    except Exception as ex:
        print(ex)
        return  JsonResponse({'return': 1}, safe=False)





    # for art  in Article_queryset:
    #     temp = model_to_dict(art)  # 将一个queryset对象转化为  字典
    #     Article_list.append(temp)
    print(Article_list)
    return JsonResponse({'articleList': 1},safe=False)
    

