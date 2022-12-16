'''
Author: Zongzi haolin1021@gmail.com
Date: 2022-12-16 13:29:54
LastEditors: Zongzi haolin1021@gmail.com
LastEditTime: 2022-12-16 13:34:33
FilePath: /blog/typeidea/typeidea/wsgi.py
Description: 
'''
"""
WSGI config for typeidea project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'typeidea.settings.develop')

application = get_wsgi_application()
