from django.contrib import admin

# Register your models here.

from blog.models import NavTitle, Article, Resume, Power,Site

admin.site.register(NavTitle)
admin.site.register(Article)
admin.site.register(Resume)
admin.site.register(Power)
admin.site.register(Site)