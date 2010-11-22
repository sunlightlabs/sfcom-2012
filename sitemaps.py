from django.contrib.auth.models import User
from django.contrib.sitemaps import Sitemap, FlatPageSitemap
from django.core.urlresolvers import reverse
from sunlightfoundation.policy.models import PolicyPaper
from sunlightfoundation.presscenter.models import PressArticle, PressRelease
from wordpress.models import Post
import itertools

class BlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5
    
    def items(self):
        return Post.objects.published()
    
    def lastmod(self, obj):
        return obj.post_date

class PolicyPaperSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5
    
    def items(self):
        return PolicyPaper.objects.filter(published=True)
    
    def location(self, obj):
        return reverse('policy_document', args=(obj.slug,))

class PressSitemap(Sitemap):
    changefreq = "never"
    priority = 0.3
    
    def items(self):
        return [o for o in itertools.chain(
            PressRelease.objects.filter(is_public=True),
            PressArticle.objects.filter(is_public=True),
        )]
    
    def lastmod(self, obj):
        return obj.date_posted

class StaffSitemap(Sitemap):
    changefreq = "never"
    priority = 0.4
    
    def items(self):
        return User.objects.filter(is_active=True, groups__name__in=(
            'Staff - Consultants',
            'Staff - Founders',
            'Staff - General',
            'Staff - Interns',
            'Staff - Strategic Consultants',
        ))
    
    def location(self, obj):
        return reverse('people_detail', args=(obj.username,))
    

class StaticSitemap(Sitemap):
    
    pages = [
        {'path': '/about/', 'priority': 0.7},
        {'path': '/about/board/', 'priority': 0.6},
        {'path': '/about/funding/', 'priority': 0.7, 'changefreq': 'monthly'},
        {'path': '/about/grants/', 'priority': 0.7, 'changefreq': 'monthly'},
        {'path': '/about/history/'},
        {'path': '/contact/', 'priority': 0.3, 'changefreq': 'never'},
        {'path': '/donate/', 'priority': 0.7},
        {'path': '/earmarkdisclosures/2009/', 'priority': 0.4, 'changefreq': 'never'},
        {'path': '/earmarkdisclosures/2010/', 'priority': 0.4, 'changefreq': 'never'},
        {'path': '/mailinglist/', 'priority': 0.3, 'changefreq': 'never'},
        {'path': '/people/', 'priority': 0.6},
        {'path': '/policy/'},
        {'path': '/policy/poia/'},
        {'path': '/policy/success/'},
        {'path': '/press/'},
        {'path': '/press/experts/', 'priority': 0.7, 'changefreq': 'monthly'},
        {'path': '/projects/', 'priority': 0.8, 'changefreq': 'weekly'},
        {'path': '/', 'priority': 1.0, 'changefreq': 'hourly'},
    ]
    
    def items(self):
        return self.pages
    
    def location(self, obj):
        return obj.get('path')
    
    def changefreq(self, obj):
        return obj.get('changefreq', 'never')
    
    def priority(self, obj):
        return obj.get('priority', '0.5')


sitemaps = {
    'blog': BlogSitemap,
    'flatpages': FlatPageSitemap,
    'policy': PolicyPaperSitemap,
    'press': PressSitemap,
    'staff': StaffSitemap,
    'static': StaticSitemap,
}