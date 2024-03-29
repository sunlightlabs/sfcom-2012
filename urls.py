from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import direct_to_template
from sunlightfoundation.com.feeds import NetworkFeed, NetworkOnlyFeed
from sunlightfoundation.presscenter.feeds import PressArticleFeed, PressReleaseFeed
from thefoundation.feeds import BlogFeed
from thefoundation.sitemaps import sitemaps

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^about/funding/$', 'thefoundation.views.funding', name='funding'),
    url(r'^admin/django-lean/', include('django_lean.experiments.admin_urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('wordpress.urls')),
    url(r'^contact/', 'thefoundation.views.contact', name='contact'),
    url(r'^django-lean/', include('django_lean.experiments.urls')),
    url(r'^donate/payment/', include('simplepay.urls')),
    url(r'^donate/', include('sunlightfoundation.donations.urls')),
    url(r'^earmarkdisclosures/', include('sunlightfoundation.earmarkdisclosures.urls')),
    url(r'^f/', include('sunlightfoundation.signups.urls')),
    url(r'^mailinglist/', include('sunlightfoundation.spammer.urls')),
    url(r'^policy/', include('sunlightfoundation.policy.urls')),
    url(r'^press/experts/$', 'django.views.generic.simple.direct_to_template', {"template": "presscenter/experts.html"}),
    url(r'^press/logos/$', 'django.views.generic.simple.direct_to_template', {"template": "presscenter/logos.html"}),
	url(r'^press/', include('sunlightfoundation.presscenter.urls')),
    url(r'^projects/$', 'thefoundation.views.projects', name='projects'),
    url(r'^search/', include('haystack.urls')),
    url(r'^staff/', include('googleauth.urls')),
    url(r'^staff/', include('sunlightfoundation.staff.urls')),
    url(r'^superpacs/', include('sunlightfoundation.superpacs.urls')),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    url(r'^', include('mediasync.urls')),
    url(r'^', include('thefoundation.legacy.urls')),
    url(r'^$', 'thefoundation.views.index', name='index'),
)

# top level navigation redirects
urlpatterns += patterns('django.views.generic.simple',
    #url(r'^blog/',      'redirect_to', {'url': 'http://blog.sunlightfoundation.com/'}),
    url(r'^campaign/',          'redirect_to', {'url': 'http://publicequalsonline.com/'}),
    url(r'^labs/',              'redirect_to', {'url': 'http://sunlightlabs.com/'}),
    url(r'^reporting/',         'redirect_to', {'url': 'http://reporting.sunlightfoundation.com/'}),
    url(r'^people/cjohnson/$',  'redirect_to', {'url': 'http://infovegan.com', 'permanent': True}),
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
    url(r'^about/grants/$', 'direct_to_template', {"template": "about/grants.html"}),
    url(r'^about/history/$', 'direct_to_template', {"template": "about/history.html"}),
    url(r'^policy/poia/about/$', 'direct_to_template', {"template": "policy/poia_about.html"}),
    url(r'^policy/success/$', 'direct_to_template', {"template": "policy/success.html"}),
    url(r'^legal/privacy/$', 'direct_to_template', {"template": "legal/privacy.html"}),
    url(r'^legal/terms/$', 'direct_to_template', {"template": "legal/terms.html"}),
    url(r'^infographics/bluedog-fire-2009/$', 'direct_to_template', {"template": "infographics/bluedog-fire-2009.html"}),
    url(r'^infographics/dodd-shelby/$', 'direct_to_template', {"template": "infographics/dodd-shelby.html"}),
    url(r'^infographics/healthsectorcontributions/$', 'direct_to_template', {"template": "infographics/healthsectorcontributions.html"}),
    url(r'^infographics/reconciliation/$', 'direct_to_template', {"template": "infographics/reconciliation.html"}),
    url(r'^infographics/senate-fire-ag/$', 'direct_to_template', {"template": "infographics/senate-fire-ag.html"}),
    url(r'^infographics/telecom-lobby/$', 'direct_to_template', {"template": "infographics/telecom-lobby.html"}),
    url(r'^infographics/lincoln/energy/$', 'direct_to_template', {"template": "infographics/lincoln_energy.html"}),
    url(r'^join/thankyou/$', 'direct_to_template', {"template": "clean/thankyou.html"}),
    url(r'^live/$', 'direct_to_template', {"template": "live/live.html"}),
    url(r'^live/feedback$', 'direct_to_template', {"template": "live/feedback.html"}),
	url(r'^opengovernmentdirective/$', 'direct_to_template', {"template": "opengovernmentdirective.html"}),
	url(r'^presentations/$', 'direct_to_template', {"template": "presentations/index.html"}),
	url(r'^presentations/emillerMITjune2010/$', 'direct_to_template', {"template": "presentations/emillerMITjune2010.html"}),
	url(r'^projects/2009/earmarks/no_disclosure/$', 'direct_to_template', {"template": "projects/2009/earmarks/no_disclosure.html"}),
	url(r'^projects/2009/expenditures/$', 'direct_to_template', {"template": "projects/2009/expenditures/index.html"}),
	url(r'^projects/2009/healthcare_lobbyist_complex', 'direct_to_template', {"template": "projects/2009/healthcare_lobbyist_complex.html"}),
	url(r'^projects/2009/heart_of_the_matter', 'direct_to_template', {"template": "projects/2009/heart_of_the_matter.html"}),
	url(r'^projects/2009/oogl', 'direct_to_template', {"template": "projects/2009/oogl.html"}),
	url(r'^tmp/heart', 'direct_to_template', {"template": "projects/2009/heart_of_the_matter.html"}),
	url(r'^topics/BP/GulfOilSpill/$', 'direct_to_template', {"template": "topics/BP/GulfOilSpill/index.html"}),
	url(r'^topics/BP/GulfOilSpill/reform/markup/$', 'direct_to_template', {"template": "topics/BP/GulfOilSpill/reform/markup.html"}),
	url(r'^topics/citizensunited', 'direct_to_template', {"template": "topics/citizensunited.html"}),
	url(r'^topics/earmarks', 'direct_to_template', {"template": "topics/earmarks.html"}),
	url(r'^topics/financial-reform', 'direct_to_template', {"template": "topics/financial-reform.html"}),

)

# projects - to be made into a real django app
urlpatterns += patterns('django.views.generic.simple',
    url(r'^projects/congress-for-android/$', 'direct_to_template', {"template": "projects/congress-for-android.html"}),
)

# primary redirects
urlpatterns += patterns('django.views.generic.simple',
    url(r'^android/congress/', 'redirect_to', {'url': '/projects/congress-for-android/'}),
    url(r'^campaigns/$', 'redirect_to', {'url': '/projects/'}),
    url(r'^campaigns/pass482/', 'redirect_to', {'url': 'http://sunlightfoundation.com/pass482/'}),
    url(r'^campaigns/publicequalsonline/', 'redirect_to', {'url': 'http://publicequalsonline.com'}),
    url(r'^campaigns/readthebill/', 'redirect_to', {'url': 'http://readthebill.org'}),
    url(r'^citizensunited/$', 'redirect_to', {'url': '/donate/'}),
    url(r'^contact/thanks/$', 'direct_to_template', {"template": "contact_thanks.html"}),
    url(r'^financial-reform/', 'redirect_to', {'url': '/projects/2010/financial-reform/'}),
    url(r'^grants/application/thanks/$', 'direct_to_template', {"template": "grant_application_thanks.html"}),
    url(r'^grants/minigrantapplication/', 'redirect_to', {'url': '/grants/application/'}),
    url(r'^holiday2008/swfobject.js$', 'direct_to_template', {"template": "projects/2008/holiday2008/swfobject.js", "mimetype": "text/javascript"}),
    url(r'^holiday2008/$', 'direct_to_template', {"template": "projects/2008/holiday2008/index.html"}),
    url(r'^logos/$', 'redirect_to', {'url': '/press/logos/'}),
    url(r'^projects/2006/earmarks/$', 'direct_to_template', {"template": "projects/2006/earmarks/index.html"}),
    url(r'^projects/2007/punchclockmap/$', 'direct_to_template', {"template": "projects/2007/punchclockmap/punchclock.html"}),
    url(r'^projects/2009/expenditures/', 'redirect_to', {'url': '/projects/2009/expenditures/'}), # flatpage
    url(r'^projects/2009/expenditures/totals', 'redirect_to', {'url': '/projects/2009/expenditures/'}), # flatpage
    url(r'^projects/2009/expenditures/committees', 'redirect_to', {'url': '/projects/2009/expenditures/'}), # flatpage
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
    url(r'^feeds/blog/$', BlogFeed()),
    url(r'^feeds/latest/$', NetworkFeed()),
    url(r'^feeds/network/$', NetworkOnlyFeed()),
    url(r'^feeds/pressarticles/$', PressArticleFeed()),
    url(r'^feeds/pressreleases/$', PressReleaseFeed()),
)

# feed redirects
urlpatterns += patterns('django.views.generic.simple',
    url(r'^rss.xml', 'redirect_to', {'url': '/feeds/latest/'}),
    url(r'^aggregator/', 'redirect_to', {'url': '/feeds/latest/'}),
    url(r'^atom/feed/', 'redirect_to', {'url': '/feeds/blog/'}),
    url(r'^blog/feed/', 'redirect_to', {'url': '/feeds/blog/'}),
    url(r'^blog/atom/', 'redirect_to', {'url': '/feeds/blog/'}),
    url(r'^feed/sunlightblogs.php', 'redirect_to', {'url': '/feeds/network/'}),
    url(r'^feed/sunlightpressrelease.php', 'redirect_to', {'url': '/feeds/pressreleases/'}),
    url(r'^feed/sunlightpress.php', 'redirect_to', {'url': '/feeds/pressarticles/'}),
    url(r'^feed/ethics.php', 'redirect_to', {'url': '/feeds/congressional_news/'}),
    url(r'^feed/', 'redirect_to', {'url': '/feeds/latest/'}),
)