'''
Author: Zongzi haolin1021@gmail.com
Date: 2022-12-19 14:11:32
LastEditors: Zongzi haolin1021@gmail.com
LastEditTime: 2022-12-19 14:13:39
FilePath: /blog/typeidea/blog/adminforms.py
Description: 
'''
from django import forms

class PostAdminForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea, label ='摘要', required=False)