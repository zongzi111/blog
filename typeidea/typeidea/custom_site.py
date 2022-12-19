'''
Author: Zongzi haolin1021@gmail.com
Date: 2022-12-19 14:24:01
LastEditors: Zongzi haolin1021@gmail.com
LastEditTime: 2022-12-19 14:26:02
FilePath: /blog/typeidea/typeidea/custom_site.py
Description: 
'''
from django.contrib.admin import AdminSite

class CustomSite(AdminSite):
    site_header = 'Typeidea'
    site_title = 'Typeodea管理后台'
    index_title = '首页'

custom_site = CustomSite(name = 'cus_admin')