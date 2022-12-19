'''
Author: Zongzi haolin1021@gmail.com
Date: 2022-12-16 14:4de4:57
LastEditors: Zongzi haolin1021@gmail.com
LastEditTime: 2022-12-19 16:56:02
FilePath: /blog/typeidea/blog/admin.py
Description: 
'''
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Post, Category, Tag
from .adminforms import PostAdminForm
from typeidea.custom_site import custom_site
from typeidea.base_admin import BaseOwnerAdmin
# Register your models here.

class PostInline(admin.TabularInline):
    fields = ('title', 'desc')
    extra = 1
    model = Post

@admin.register(Category, site=custom_site)
class CategoryAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'is_nav', 'owner', 'created_time', 'post_count')
    fields = ('name', 'status', 'is_nav')
    inlines = [PostInline,]
    def post_count(self, obj):
        return obj.post_set.count()
    post_count.short_description = '文章数量'

@admin.register(Tag, site=custom_site)
class TagAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'owner', 'created_time')
    fields = ('name', 'status')

class CategoryOwnerFilter(admin.SimpleListFilter):
    title = '分类过滤器'
    parameter_name = 'owner_category'
    
    def lookups(self, request, model_admin):
        return Category.objects.filter(owner=request.user).values_list('id', 'name')
    
    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=self.value())
        return queryset

@admin.register(Post, site=custom_site)
class PostAdmin(BaseOwnerAdmin):
    form = PostAdminForm
    list_display = (
        'title', 'category', 'status',
        'created_time', 'owner', 'operator'
    )
    list_display_links=[]
    
    list_filter = [CategoryOwnerFilter]
    search_fields = ['title', 'category']

    actions_on_top = True
    actions_on_bottom = True
    
    #编辑页面
    save_on_top = True

    exclude = ('owner',)
    
    # fields = (
    #     'category', 'title',
    #     'desc',
    #     'status',
    #     'content',
    #     'tag',
    # )

    fieldsets = (
        ('基础配置', {
            'description': '基础配置描述',
            'fields':(
                ('title', 'category'),
                'status',
            ),
        }),
        ('内容', {
            'fields':(
                'desc',
                'content',
            ),
        }),
        ('额外信息', {
            'classes': ('collapse',),
            'fields': ('tag',),
        })
    )


    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('cus_admin:blog_post_change', args=(obj.id,))
        )
    operator.short_description = '操作'
    
    class Media:
        css = {
            'all': ("https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css", ),
        }
        js = ('https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js', )