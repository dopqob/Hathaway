from django.contrib import admin
from myblog.models import *


# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'pub_time')    # 文章列表的显示项


admin.site.register((Category, Comment, Tag))   # 多个模块注册到后台