'''
Author: Zongzi haolin1021@gmail.com
Date: 2022-12-16 13:29:54
LastEditors: Zongzi haolin1021@gmail.com
LastEditTime: 2022-12-16 13:34:24
FilePath: /blog/typeidea/manage.py
Description: 
'''
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'typeidea.settings.develop')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
