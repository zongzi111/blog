'''
Author: Zongzi haolin1021@gmail.com
Date: 2022-12-16 14:44:57
LastEditors: Zongzi haolin1021@gmail.com
LastEditTime: 2022-12-19 16:56:32
FilePath: /blog/typeidea/comment/apps.py
Description: 
'''
from django.apps import AppConfig

class CommentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'comment'
