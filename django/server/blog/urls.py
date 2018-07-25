
from django.urls import path




from blog.views import blognavtitle
from blog.views import blog_acticle_lsit
from blog.views import views
from blog.views import blog_resume


urlpatterns = [
    path('blog/', blognavtitle.nav_title),
    path('list/', blog_acticle_lsit.blog_acticle_lsit),
    path('resume/', blog_resume.resume),
    path('test/', views.ArticleListView.as_view(), name="view_test"),
]
