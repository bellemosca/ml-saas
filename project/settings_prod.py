from os import getenv

from .settings import *

DEBUG = False
ALLOWED_HOSTS = getenv('ALLOWED_HOSTS', '*').split()
SECRET_KEY = getenv('SECRET_KEY', SECRET_KEY)
