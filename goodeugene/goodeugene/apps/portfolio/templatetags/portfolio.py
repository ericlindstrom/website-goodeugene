from django import template 
from django.shortcuts import render_to_response
from apps.portfolio.models import *

register = template.Library()

@register.inclusion_tag('portfolio/tag_portfolio_list.html')
def portfolio_list():
    items = Project.objects.filter(visible=True)
    return {'items' : items }