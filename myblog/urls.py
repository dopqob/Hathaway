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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view()),
    path('category/<int:category>', views.CategoryList.as_view(), name='category'),
    path('search/', views.Search.as_view(), name='search'),
    path('detail/<int:pk>', views.ArticleDetail.as_view(), name='detail'),
    path('comment/', views.pub_comment, name='comment'),
    path('summernote/', views.summernote),  # 测试前台summernote富文本编辑器
]
