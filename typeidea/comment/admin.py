'''
Author: Zongzi haolin1021@gmail.com
Date: 2022-12-16 14:44:57
LastEditors: Zongzi haolin1021@gmail.com
LastEditTime: 2022-12-19 17:04:47
FilePath: /blog/typeidea/comment/admin.py
Description: 
'''
from django.contrib import admin
from django.contrib.admin.models import LogEntry

from .models import Comment
from typeidea.custom_site import custom_site


# Register your models here.

@admin.register(Comment, site=custom_site)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('target', 'nickname', 'content', 'website', 'created_time')

@admin.register(LogEntry, site=custom_site)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['object_repr', 'object_id', 'action_flag', 'user', 'change_message']