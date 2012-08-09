from django.views.generic import TemplateView, ListView, DetailView
from django.conf import settings
from models import *

class PortfolioIndex(ListView):
    model = Project
    template_name = 'portfolio/project_list.html'

    def get_queryset(self):
	return Project.objects.live()

    def get_template_names(self):
	#return [ 
	#    'portfolio/index_%s.html' % settings.PORTFOLIO_VIEW, 
	#    self.template_name,
	#]
	try:
	    return 'portfolio/index_%s.html' % settings.PORTFOLIO_VIEW
	except AttributeError:
	    return self.template_name


class PortfolioCategory(ListView):
    model = Category

    def get_queryset(self):
	return Category.objects.live() 


class PortfolioClient(ListView):
    model = Project

    def get_queryset(self):
	return Project.objects.live().filter(client__slug=self.kwargs['client'])

class PortfolioCategoryIndex(ListView):
    model = Category

    def get_queryset(self):
	return Category.objects.live()


class PortfolioCategoryDetail(ListView):
    model = Project

    def get_queryset(self):
	return Project.objects.live().filter(client__slug=self.kwargs['category'])

class PortfolioTagIndex(ListView):
    model = Tag
    template_name = 'portfolio/category_list.html'

    def get_queryset(self):
	return Tag.objects.live()

class PortfolioTag(ListView):
    model = Project

    def get_queryset(self):
	return Project.objects.live() 


class PortfolioDetail(DetailView):
    model = Project

    def get_queryset(self):
	return Project.objects.live().filter(client__slug=self.kwargs['client'], slug=self.kwargs['slug'])
