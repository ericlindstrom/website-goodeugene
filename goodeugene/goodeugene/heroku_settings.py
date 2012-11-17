from settings import *
import os
import dj_database_url
from memcacheify import memcacheify


DEBUG = False

#Database
DATABASES = {'default': dj_database_url.config(default=os.environ['DATABASE_URL'])}

#caches
CACHES = memcacheify()

#Storage
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_ACCESS_KEY_ID = os.environ['S3_KEY']
AWS_SECRET_ACCESS_KEY = os.environ['S3_SECRET'] 
AWS_STORAGE_BUCKET_NAME = 'public.goodeugene.com'
AWS_QUERYSTRING_ACTIVE = True
AWS_QUERYSTRING_AUTH = False
AWS_S3_SECURE_URLS = False
#AWS_IS_GZIPPED = True

STATIC_URL = 'http://%s/static/' % AWS_STORAGE_BUCKET_NAME
MEDIA_URL = 'http://%s/media/' % AWS_STORAGE_BUCKET_NAME
ADMIN_MEDIA_PREFIX = '%sadmin/' % STATIC_URL

DEFAULT_FILE_STORAGE = 'goodeugene.util.s3.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'goodeugene.util.s3.StaticRootS3BotoStorage'


