from django.core.management.base import BaseCommand, CommandError
import sys
from optparse import make_option
from goodeugene.apps.portfolio.models import *
from django.conf import settings

class Command(BaseCommand):
    help='''Import json file'''
    option_list = BaseCommand.option_list + (
        make_option('--file',
            help='json_file'),
        )
   
    def handle(self, **options):
	run_import(options['file'])

def run_import(json_file):
    import json, urllib
    json_data = open(json_file)
    data = json.load(json_data)
    for i in data:
        try:
            c = Client.objects.get(slug=i['client_slug'])
        except:
            c = Client(
                name = i['client'],
                slug = i['client_slug'],
            )
            c.save()
	
	order_num = i['order_num'] if i['order_num'] else 100

	p_name = i['name'] if i['name'] else i['client']
	p_slug = i['slug'] if i['slug'] else i['client_slug']

	try:
	    p = Project.objects.get(slug=p_slug, client__slug=i['client_slug'])
	except:
	    p = Project(
		client = c,
		name = p_name,
		slug = p_slug,
		description = i['details'],
		order = order_num,
		visible = i['visible'],
	    )
	    p.save()
	print p.client.name , p.name

	num_photos = i['num_photos']
	num = 1
	while num <= num_photos:
	    img = 'portfolio/project/display/%s%s.jpg' % (i['photo_name'], num)
	    try:
		newimage = Image.objects.get(display=img)
	    except:
		newimage = Image(
		    display = img,
		    order = 10*num,
		    project = p,
		
		)
		newimage.save()
	    num = num+1
	
