import sys
import json

FILE_DIR = '_posts/'

def build_front_matter(item):
    if item['name'] == None:
	item['name'] = ''
    html = '''---
layout: page
title: %(client)s %(name)s
type: projects
permalink: /projects/%(client_slug)s/%(slug)s/
thumb: /media/images/%(photo_name)s-thumb.jpg
description: %(details)s
---
''' % item
    return html

def build_content(item):
    images = []
    photo = 1
    while photo <= item['num_photos']:
	images.append('![](/media/images/%s%s.jpg)' % (item['photo_name'], photo,))
	photo = photo+1

    if item['details'] == None or item['details'] == 'null':
	item['details'] = ''

    html = '''%(content)s

%(images)s''' % { 'content': item['details'], 'images': '\n'.join(images)}

    return html

def make_files(input_file):
    json_data = open(input_file)
    data = json.load(json_data)
    for item in data:
	html = [
	    build_front_matter(item),
	    build_content(item)
	]
    
	if item['order_num'] == None:
	    item['order_num'] = 0

	if len(str(item['order_num'])) == 1:
	    item['order_num'] = '30%d0' % item['order_num']
	if len(str(item['order_num'])) == 2:
	    item['order_num'] = '3%d0' % item['order_num']

	if not item['slug']:
	    item['slug'] = 'no-slug%d' % item['id']
	
	item['filepath'] = FILE_DIR
	filename = '%(filepath)s%(order_num)s-01-01-%(slug)s.md' % item
	f = open(filename, 'w+')
	print 'writing %s' % filename
	f.write('\n'.join(html))
	f.close()
	
    json_data.close()
   

if __name__ == '__main__':
    make_files(sys.argv[1])
