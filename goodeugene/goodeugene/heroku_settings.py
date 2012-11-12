from settings import *
import os
import dj_database_url

DEBUG = False
DATABASES = {'default': dj_database_url.config(default=os.environ['DATABASE_URL'])}

PUBLIC_SITE = 'public.goodeugene.com'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_ACCESS_KEY_ID = os.environ['S3_KEY']
AWS_SECRET_ACCESS_KEY = os.environ['S3_SECRET'] 
AWS_STORAGE_BUCKET_NAME = PUBLIC_SITE
AWS_QUERYSTRING_ACTIVE = True
#AWS_QUERYSTRING_AUTH = False
AWS_S3_SECURE_URLS = False
#AWS_IS_GZIPPED = True

STATIC_URL = 'http://%s/static/' % PUBLIC_SITE
MEDIA_URL = 'http://%s/media/' % PUBLIC_SITE
ADMIN_MEDIA_PREFIX = 'http://%s/admin/' % PUBLIC_SITE

DEFAULT_FILE_STORAGE = 'goodeugene.util.s3.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'goodeugene.util.s3.StaticRootS3BotoStorage'
