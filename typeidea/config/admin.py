'''
Author: Zongzi haolin1021@gmail.com
Date: 2022-12-16 14:44:57
LastEditors: Zongzi haolin1021@gmail.com
LastEditTime: 2022-12-19 16:57:25
FilePath: /blog/typeidea/config/admin.py
Description: 
'''
from django.contrib import admin

from .models import Link, SideBar
from typeidea.custom_site import custom_site
from typeidea.base_admin import BaseOwnerAdmin

# Register your models here.

@admin.register(Link, site=custom_site)
class LinkAdmin(BaseOwnerAdmin):
    list_display = ('title', 'href', 'status', 'weight', 'created_time')
    fields = ('title', 'href', 'status', 'weight')

@admin.register(SideBar, site=custom_site)
class SideBarAdmin(BaseOwnerAdmin):
    list_display = ('title', 'display_type', 'content', 'created_time')
    fields = ('title', 'display_type', 'content')