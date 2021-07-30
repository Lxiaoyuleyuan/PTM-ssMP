"""
WSGI config for ptmpt project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""
import os
from django.core.wsgi import get_wsgi_application
import sys
from os.path import join,dirname,abspath 
sys.path.append("/home/bmi/wwwroot/PTM-ssMP/ptmpt")
# sys.path.append("/home/bmi/wwwroot/ptmpt")
# sys.path.append("/home/bmi/wwwroot/")
PROJECT_DIR = dirname(dirname(abspath(__file__)))
sys.path.insert(0, PROJECT_DIR)
os.environ["DJANGO_SETTINGS_MODULE"] = "ptmpt.settings"
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ptmpt.settings")
# import django.core.handlers.wsgi
# application = django.core.handlers.wsgi.WSGIHandler()
application = get_wsgi_application()
