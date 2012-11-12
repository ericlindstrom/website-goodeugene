from django.db import models
from app_settings import NO_IMAGE, NON_WORK

class PortfolioManager(models.Manager):
    def live(self):
	return super(PortfolioManager, self).get_query_set().filter(visible=True)

    def featured(self):
	return super(PortfolioManager, self).live(featured=True)

class PortfolioBase(models.Model):
    name = models.CharField(max_length=255, null=True)
    slug = models.SlugField(null=True, blank=True)
    order = models.IntegerField(default=100)
    visible = models.BooleanField(default=True)
    featured = models.BooleanField(default=True)

    objects = PortfolioManager()

    class Meta:
	abstract = True

    def __unicode__(self):
        return self.name

class Tag(PortfolioBase):
    class Meta:
	verbose_name_plural = 'Tags'

    @models.permalink
    def get_absolute_url(self):
	return('portfolio:tag-detail', (), {
	    'tag': self.slug,
	})

class Category(PortfolioBase):
    class Meta:
        verbose_name_plural = 'Categories'

    @models.permalink
    def get_absolute_url(self):
        return('portfolio:category-detail', (), {'category': self.slug })

class Client(PortfolioBase):
    thumbnail = models.ImageField(upload_to='images/client/thumb/', blank=True)
    
    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Client'

    @models.permalink
    def get_absolute_url(self):
	return('portfolio:client-detail', (), {
	    'client': self.slug,
	})


class Role(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    
    def __unicode__(self):
        return self.title

class Credit(models.Model):
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    url = models.URLField(verify_exists=False, blank=True)

    def __unicode__(self):
        return '%s: %s' % (self.title, self.name)

class Project(PortfolioBase):
    client =  models.ForeignKey(Client, blank=True, null=True)
    role = models.ForeignKey(Role, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, blank=True, null=True)
    credits = models.ManyToManyField(Credit, blank=True)
    url = models.CharField(max_length=255, blank=True)
    #tags = models.ManyToManyField(Tag, blank=True)

    thumbnail = models.ImageField(upload_to='portfolio/projects/thumb/', blank=True)

    
    def project_admin_title(self):
	return self.name

    def full_project_title(self):
	return '%s %s' % (self.client.name, self.name,)

    def get_thumbnail(self):
        thumb = NO_IMAGE['thumbnail']
	try:
	    thumb=self.image_set.all()[0].get_image_for_list()
	except IndexError:
	    pass
	#print self.thumbnail
        #if self.thumbnail: 
	#    thumb = self.thumbnail
	#else:
	#    thumb = self.image_set.all()[0].get_image_for_list()
	return thumb
    
    @models.permalink
    def get_absolute_url(self):
	if self.client:	
	    return('portfolio:project-detail', (), {
		'client': self.client.slug,
		'slug': self.slug,
	    })
	else:
	    return('portfolio:project-detail', (), {
		'client': NON_WORK['slug'],
		'slug': self.slug,
	    })
        

class Image(models.Model):
    full_size = models.ImageField(upload_to='portfolio/project/full/', blank=True)
    display = models.ImageField(upload_to='portfolio/project/display/', blank=True)
    thumb = models.ImageField(upload_to='portfolio/project/thumb/', blank=True)
    title = models.CharField(max_length=255, blank=True)
    order = models.FloatField(default=0)
    project = models.ForeignKey(Project)

    #TODO: Reprocess from fullsize
    def get_image_for_list(self):
	if self.thumb:
	    return self.thumb
	elif self.display:
	    return self.display
	elif self.full_size:
	    return self.full_size

    def get_image_for_detail(self):
	if self.full_size:
	    return self.full_size
	elif self.display:
	    return self.display


    
    
    #def __unicode__(self):
    #    return self.thumb
    
class Video(models.Model):
    video = models.FileField(upload_to='videos')
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField()
    project = models.ForeignKey(Project)

    def __unicode__(self):
        return self.title
