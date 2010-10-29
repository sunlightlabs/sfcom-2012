from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('django.views.generic.simple',
    # about pages
    url(r'^board_of_directors/$', 'redirect_to', {'url': '/about/board/', 'permanent': True}),
    url(r'^funding/$', 'redirect_to', {'url': '/about/funding/', 'permanent': True}),
    
    # press
    url(r'^presscenter(?P<path>.*)', 'redirect_to', {'url': '/press%(path)s', 'permanent': True}),
)