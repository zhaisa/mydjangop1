import Record as Record
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from demo01.models import Blog,Blogcon
from django.db import models
from django.utils.html import format_html


# # Blog模型的管理器
# class BlogAdmin(admin.ModelAdmin):
#     list_display = ('id', 'caption', 'author', 'publish_time')
#
#
# # 在admin中注册绑定
# admin.site.register(Blog, BlogAdmin)


# Blog模型的管理器
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('id', 'caption', 'author', 'publish_time')

    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 20

    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('-publish_time',)

    # list_editable 设置默认可编辑字段
  #  list_editable = ['machine_room_id', 'temperature']

    # fk_fields 设置显示外键字段
  #  fk_fields = ('machine_room_id',)
@admin.register(Blogcon)
class BlogcoAdmin(admin.ModelAdmin):
    list_display = ('machine_room_id','use','status','head','type','memory','cpu','cipan','operating','belonghouse','belonggroup')
    list_per_page = 10


class MyAdminSite(admin.AdminSite):
    admin.site.site_header = '融贝测试管理系统'  # 此处设置页面显示标题
    admin.site.site_title = '融贝测试'  # 此处设置页面头部标题


