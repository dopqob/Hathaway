#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/18 16:26
# @Author  : Bilon
# @File    : adminx.py
import xadmin
from xadmin import views
from .models import *


class GlobalSetting(object):    # 更改后台Tttle和页脚说明
    """全局设置"""
    site_title = '躲雨の屋檐'
    site_footer = '躲雨の屋檐 基于Django构建 · © 2018-2020'
    menu_style = 'accordion'    # 菜单展开收起效果

    # 菜单
    def get_site_menu(self):
        return [
            {
                'title': 'APP测试',
                # 'perm': self.get_model_perm(Service, 'view'),
                'menus': (
                    {
                        'title': '订单',
                        'url': 'http://127.0.0.1:8001/',
                    },
                    {
                        'title': '客户',
                        'url': 'http://127.0.0.1:8001/',
                    },
                )
            },
        ]

class ArticleAdmin(object):
    list_display = ('title', 'category', 'pub_time')    # 文章列表的显示项
    search_fields = ('title','author')  # 搜索框
    # list_filter = ['author']  # 过滤器
    style_fields = {'content':'ueditor'}


xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(Category)
xadmin.site.register(Comment)
xadmin.site.register(Tag)
# xadmin.site.register((Category, Comment, Tag))   # 多个模块注册到后台
