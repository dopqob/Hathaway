"""Hathaway URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from Hathaway import settings
import xadmin

urlpatterns = [
    path('ueditor/',include('DjangoUeditor.urls')),  # 富文本编辑器Ueditor
    path('summernote', include('django_summernote.urls')),  # 富文本编辑器SummerNote
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),   # 用于上传图片文件
    path('static/<path:path>', serve, {'document_root': settings.STATIC_ROOT}), # 用于加载静态文件
    path('admin/', admin.site.urls),    # 系统自带后台
    path('xadmin/', xadmin.site.urls),   # 使用xadmin后台
    path('', include('myblog.urls'))
]
