'''
Author: Zongzi haolin1021@gmail.com
Date: 2022-12-16 14:19:04
LastEditors: Zongzi haolin1021@gmail.com
LastEditTime: 2022-12-16 14:38:46
FilePath: /blog/home/data/nas/code/django/blog/typeidea/comment/models.py
Description: 
'''
from django.db import models

from blog.models import Post

# Create your models here.
class Comment(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )
    target = models.ForeignKey(Post, verbose_name="评论目标", on_delete=models.CASCADE)
    content = models.CharField(max_length=2000, verbose_name="内容")
    nickname = models.CharField(max_length=50, verbose_name="昵称")
    website = models.URLField(verbose_name="网站")
    email = models.EmailField(verbose_name="邮箱")
    status = models.PositiveIntegerField(default=STATUS_NORMAL,
        choices=STATUS_ITEMS, verbose_name="状态")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    
    class Meta:
        verbose_name = verbose_name_plural = "评论"