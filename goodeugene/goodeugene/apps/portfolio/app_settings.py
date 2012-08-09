from django.conf import settings

STATIC_URL = getattr(settings,'STATIC_URL', '/static/')

NO_IMAGE = {
    'thumbnail': {
	'url': getattr(settings, 'NO_THUMBNAIL', STATIC_URL + 'portfolio/img/no_thumbnail.jpg'),
    },
    'display': {
	'url': STATIC_URL + 'portfolio/img/no_display.jpg',
    },
}

