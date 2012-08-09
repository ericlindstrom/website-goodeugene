from django.conf.urls.defaults import *
from views import *

from django.views.generic import RedirectView

#find a better way to redirect /category/
#print reverse('category-index')

urlpatterns = patterns('',
    url(r'^category/(?P<category>.*)/$', PortfolioCategoryDetail.as_view(), name='category-detail'),
    url(r'^categories/$', PortfolioCategoryIndex.as_view(), name='category-index'),
    url(r'^category/$', RedirectView.as_view(url='/portfolio/categories/')),#redirect category -> categories

    url(r'^tag/(?P<tag>.*)/$', PortfolioTag.as_view(), name='tag-detail'),
    url(r'^tags/$', PortfolioTagIndex.as_view(), name='tag-index'),
    url(r'^tag/$', RedirectView.as_view(url='/portfolio/tags/')),#redirect tag -> tags

    url(r'^(?P<client>.*)/(?P<slug>.*)/$', PortfolioDetail.as_view(), name='project-detail'),
    url(r'^(?P<client>.*)/$', PortfolioClient.as_view(), name='client-detail'),
    url(r'^$', PortfolioIndex.as_view(), name="index"),
)

