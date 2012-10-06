# http://stackoverflow.com/questions/10390244/how-to-set-up-a-django-project-with-django-storages-and-amazon-s3-but-with-diff
from storages.backends.s3boto import S3BotoStorage
from django.utils.functional import SimpleLazyObject

StaticRootS3BotoStorage = lambda: S3BotoStorage(location='static')
MediaRootS3BotoStorage  = lambda: S3BotoStorage(location='media')
