from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import direct_to_template
from sunlightfoundation.com.feeds import NetworkFeed, NetworkOnlyFeed
from sunlightfoundation.presscenter.feeds import PressArticleFeed, PressReleaseFeed

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('wordpress.urls')),
    url(r'^contact/', 'thefoundation.views.contact', name='contact'),
    url(r'^donate/payment/', include('simplepay.urls')),
    url(r'^donate/', include('sunlightfoundation.donations.urls')),
    url(r'^earmarkdisclosures/', include('sunlightfoundation.earmarkdisclosures.urls')),
    url(r'^f/', include('sunlightfoundation.signups.urls')),
    url(r'^mailinglist/', include('sunlightfoundation.spammer.urls')),
    url(r'^policy/', include('sunlightfoundation.policy.urls')),
    url(r'^press/', include('sunlightfoundation.presscenter.urls')),
    url(r'^search/', include('haystack.urls')),
    url(r'^staff/', include('googleauth.urls')),
    url(r'^staff/', include('sunlightfoundation.staff.urls')),
    url(r'^', include('mediasync.urls')),
    url(r'^', include('thefoundation.legacy.urls')),
    url(r'^$', 'thefoundation.views.index', name='index'),
)

# top level navigation redirects
urlpatterns += patterns('django.views.generic.simple',
    #url(r'^blog/',      'redirect_to', {'url': 'http://blog.sunlightfoundation.com/'}),
    url(r'^campaign/',  'redirect_to', {'url': 'http://publicequalsonline.com/'}),
    url(r'^labs/',      'redirect_to', {'url': 'http://sunlightlabs.com/'}),
    url(r'^reporting/', 'redirect_to', {'url': 'http://reporting.sunlightfoundation.com/'}),
)

# sunlightfoundation.com module
urlpatterns += patterns('sunlightfoundation.com.views',
    url(r'^grants/application/$', 'grant_application', name='grant_application'),
    url(r'^people/$', 'people_index', name='people_list'),
    url(r'^people/(?P<username>[\w-]+)/$', 'people_detail', name="people_detail"),
    url(r'^preview/bumpers/$', 'preview_bumpers', name='preview_bumpers'),
)

# flatpages - migrate from flatpages to static files, temporarily?
urlpatterns += patterns('django.views.generic.simple',
    url(r'^about/$', 'direct_to_template', {"template": "about/index.html"}),
    url(r'^about/board/$', 'direct_to_template', {"template": "about/board.html"}),
    url(r'^about/funding/$', 'direct_to_template', {"template": "about/funding.html"}),
    url(r'^about/grants/$', 'direct_to_template', {"template": "about/grants.html"}),
    url(r'^about/history/$', 'direct_to_template', {"template": "about/history.html"}),
    url(r'^legal/privacy/$', 'direct_to_template', {"template": "legal/privacy.html"}),
    url(r'^legal/terms/$', 'direct_to_template', {"template": "legal/terms.html"}),
)


# primary redirects
urlpatterns += patterns('django.views.generic.simple',
    url(r'^contact/thanks/$', 'direct_to_template', {"template": "contact_thanks.html"}),
    url(r'^financial-reform/', 'redirect_to', {'url': '/projects/2010/financial-reform/'}),
    url(r'^grants/application/thanks/$', 'direct_to_template', {"template": "grant_application_thanks.html"}),
    url(r'^grants/minigrantapplication/', 'redirect_to', {'url': '/grants/application/'}),
    url(r'^holiday2008/swfobject.js$', 'direct_to_template', {"template": "projects/2008/holiday2008/swfobject.js", "mimetype": "text/javascript"}),
    url(r'^holiday2008/$', 'direct_to_template', {"template": "projects/2008/holiday2008/index.html"}),
    url(r'^projects/2006/earmarks/$', 'direct_to_template', {"template": "projects/2006/earmarks/index.html"}),
    url(r'^projects/2007/punchclockmap/$', 'direct_to_template', {"template": "projects/2007/punchclockmap/punchclock.html"}),
    url(r'^projects/2009/expenditures/', 'redirect_to', {'url': '/projects/expenditures/'}), # flatpage
    url(r'^projects/transparency-timeline/$', 'direct_to_template', {"template": "projects/timeline/timeline.html"}),
    # poia
    url(r'^poia/', 'redirect_to', {'url': '/policy/poia/'}),
    url(r'^thepoia/', 'redirect_to', {'url': '/policy/poia/'}),
)

# "mounted" projects
urlpatterns += patterns('',
    url(r'^projects/2007/fortune535/', include('sunlightfoundation.fortune535.urls')),
)


#
# feeds
#

# primary feeds
urlpatterns += patterns('',
    url(r'^feeds/congressional_news/', 'django.views.generic.simple.redirect_to', {'url': 'http://feeds.delicious.com/rss/Sunlight_News_Watch'}),
    url(r'^feeds/latest/$', NetworkFeed()),
    url(r'^feeds/network/$', NetworkOnlyFeed()),
    url(r'^feeds/pressarticles/$', PressArticleFeed()),
    url(r'^feeds/pressreleases/$', PressReleaseFeed()),
)

# feed redirects
urlpatterns += patterns('django.views.generic.simple',
    url(r'^rss.xml', 'redirect_to', {'url': '/feeds/latest/'}),
    url(r'^aggregator/', 'redirect_to', {'url': '/feeds/latest/'}),
    url(r'^atom/feed/', 'redirect_to', {'url': 'http://blog.sunlightfoundation.com/feed/atom/'}),
    url(r'^blog/feed/', 'redirect_to', {'url': 'http://blog.sunlightfoundation.com/feed/atom'}),
    url(r'^blog/atom/', 'redirect_to', {'url': 'http://blog.sunlightfoundation.com/feed/atom/'}),
    url(r'^feed/sunlightblogs.php', 'redirect_to', {'url': '/feeds/network/'}),
    url(r'^feed/sunlightpressrelease.php', 'redirect_to', {'url': '/feeds/pressreleases/'}),
    url(r'^feed/sunlightpress.php', 'redirect_to', {'url': '/feeds/pressarticles/'}),
    url(r'^feed/ethics.php', 'redirect_to', {'url': '/feeds/congressional_news/'}),
    url(r'^feed/', 'redirect_to', {'url': '/feeds/latest/'}),
)