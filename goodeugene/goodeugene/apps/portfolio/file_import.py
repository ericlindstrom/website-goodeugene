from xlrd import open_workbook, XL_CELL_TEXT
import sys
import os
import re
import pprint
from django.template import defaultfilters
from models import *

def excelImport(filehandle):    
    book = open_workbook(filehandle)
    
    for sheet in book.sheets():
        # print sheet.name
        # print '-' * 50
        items = []
        for row in range(sheet.nrows):
            values = []
            if row == 1: # Start with header row
                for col in range(sheet.ncols):
                    values.append(sheet.cell(row,col).value) # headers
                items.append(values)
            if row > 1:
                for col in range(sheet.ncols):
                    values.append(sheet.cell(row, col).value)
                items.append(values)

        # PROJECTS SHEET
        if sheet.name == 'Projects':
            data = []
            header_inc = 0
            h = []
            
            for item in items:
                d = {}
                if header_inc == 0:
                    for i in item:
                        h.append(i)
                else:
                    increment_item = 0
                    for j in item:
                        if h[increment_item] == 'Images':
                            pfi = re.compile(r'\s')
                            imgs = pfi.sub('', j).split(',')
                            d[h[increment_item]] = imgs
                        else:
                            d[h[increment_item]] = j
                        
                        increment_item = increment_item+1
        
                    # add to data object
                    data.append(d)
                    
                header_inc = header_inc + 1
            
    importToDB(data)

def importToDB(data):
            
    for item in data:
        # CATEGORIES
        categories = Category.objects.all()
        c_categories = []
        for category in categories: c_categories.append(category.name)
        if item['Category'] == '': item['Category'] = 'Uncategorized'
        if not item['Category'] in c_categories:
            try:
                category_item = Category(
                    name=item['Category'], 
                    slug=defaultfilters.slugify(item['Category']),
                    )
                category_item.save()
                print '[CATEGORY]: %s' % item['Category']
            except:
                print '[ERROR]: Error saving: %s' % item['Category']
        
        # CLIENTS
        clients = Client.objects.all()
        c_clients = []
        for client in clients: c_clients.append(client.name)
        if item['Client'] == '' : item['Client'] = 'Personal'
        if not item['Client'] in c_clients:
            try:
                client_item = Client(
                    name=item['Client'],
                    slug=defaultfilters.slugify(item['Client']),
                )
                client_item.save()
                print '[CLIENT]: %s' % item['Client']
            except:
                print '[ERROR]: Error saving: %s' % item['Client']

        # PROJECTS
        projects = Project.objects.all()
        c_projects = []
        for project in projects: c_projects.append([project.client.name, project.name])

        if not [item['Client'], item['Project']] in c_projects: 
            client_pk = Client.objects.get(name='Personal').pk if item['Client'] == '' else Client.objects.get(name=item['Client']).pk
            category_pk = Category.objects.get(name='Uncategorized').pk if item['Client'] == '' else Category.objects.get(name=item['Category']).pk
            publishable = 1 if item['Publishable'] == 'T' else 0

            try:
                project_item = Project(
		    visible=publishable,
		    client=Client(pk=client_pk),
		    name=item['Project'],
		    slug=defaultfilters.slugify(item['Project']),
		    description=item['Description'],
		    category=Category(pk=category_pk),
                )
                project_item.save()
                print '[PROJECT]: %s' % item['Project']
            except:
                print '[ERROR]: Error saving: %s' % item['Project']

        # IMAGES
        images = Image.objects.all()
        c_images = []
        for image in images: c_images.append(image.full_size.url.split('/')[len(image.full_size.url.split('/'))-1]) 

        project_index = Project.objects.get(client__name=item['Client'] , name=item['Project']).pk
        
        if not item['Images'][0] == '':
            for img in item['Images']:
                if not img in c_images:
                    try:
                        image_item = Image(
			     full_size='images/%s' % img,
			     project=Project(pk=project_index),
			)
                        image_item.save()
                        # TODO PROCESS display, thumb IMAGES
                        print '[IMAGE]: %s' % img
                    except:
                        print '[ERROR]: Error Saving: %s' % img

        # VIDEOS

        # ROLE
        # roles = Role.objects.all()
        # c_roles = []
        # for role in roles: c_roles.append(role)
        # 
        # roles_re = re.compile(r'^\s+|\s+\,$') # trim
        # roles_split = item['Role'].split(',') # Need the array first, probably a better way to do this
        # ii = 0
        # 
        # for i in roles_split:
        #     roles_split[ii] = roles_re.sub('',i) #return trimmed info
        #     ii = ii+1
        # 
        # if not roles_split in c_roles:
        #     for unique_role in roles_split:
        #         if not unique_role in roles:
        #             try:
        #                 role_item = Role(
        #                             title=unique_role,
        #                             slug=defaultfilters.slugify(unique_role),
        #                             )
        #                 role_item.save()
        #                 print '[ROLE]: %s' % unique_role
        #             except:
        #                 print '[ERROR]: Error Saving: %s' % role_item
            
        
        # CREDIT
        # current_credits = Credit.objects.all()
        # c_credits = []
        # for i in current_credits: c_credits.append(i)
        
    print '-' * 50
    print 'All Done!'
        


# def main():
#     print 'using: %s' % sys.argv[1]
#     excelImport(sys.argv[1])
# 
# 
# if __name__ == '__main__':
#     main()
