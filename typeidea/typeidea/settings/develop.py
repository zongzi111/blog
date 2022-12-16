'''
Author: Zongzi haolin1021@gmail.com
Date: 2022-12-16 13:31:36
LastEditors: Zongzi haolin1021@gmail.com
LastEditTime: 2022-12-16 13:33:11
FilePath: /blog/typeidea/typeidea/settings/develop.py
Description: 
'''
from .base import *  #NOQA
# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
