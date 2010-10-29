from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('django.views.generic.simple',
    url(r'^presscenter(?P<path>.*)', 'redirect_to', {'url': '/press%(path)s'}),
)