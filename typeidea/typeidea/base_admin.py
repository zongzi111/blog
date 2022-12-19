'''
Author: Zongzi haolin1021@gmail.com
Date: 2022-12-19 16:47:31
LastEditors: Zongzi haolin1021@gmail.com
LastEditTime: 2022-12-19 16:51:33
FilePath: /blog/typeidea/typeidea/base_admin.py
Description: 
'''
from django.contrib import admin

class BaseOwnerAdmin(admin.ModelAdmin):
    exclude = ('owner',)

    def get_queryset(self, request):
        qs = super(BaseOwnerAdmin, self).get_queryset(request)
        return qs.filter(owner=request.user)
    
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(BaseOwnerAdmin).save_model(request, obj, form, change)