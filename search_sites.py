from django.contrib.flatpages.models import FlatPage
from feedinator.models import FeedEntry
from haystack import site
from haystack import indexes
from sunlightfoundation.presscenter.models import PressArticle, PressRelease
from wordpress.models import Post

#
# WordPress
#

class WordPressIndex(indexes.SearchIndex):
    type = indexes.CharField(default='post')
    text = indexes.CharField(document=True, model_attr='content', use_template=True)
    summary = indexes.CharField(model_attr='excerpt')
    title = indexes.CharField(model_attr='title') 
    link = indexes.CharField(model_attr='get_absolute_url')
    def get_queryset(self):
        return Post.objects.published()
site.register(Post, WordPressIndex)    
    
#
# django feedinator
#

EXCLUDED_FEEDS = ('delicious-sunlightmedia','congresspedia','delicious-sunlightnewswatch',
                  'opensecrets','reporting','sunlightfoundation')

class FeedEntryIndex(indexes.SearchIndex):
    type = indexes.CharField(default='feed')
    text = indexes.CharField(document=True, model_attr='content', use_template=True)
    summary = indexes.CharField(model_attr='summary')
    feed = indexes.CharField(model_attr='feed')
    title = indexes.CharField(model_attr='title') 
    link = indexes.CharField(model_attr='link')
    author = indexes.CharField(model_attr='author_name')
    def get_queryset(self):
        return FeedEntry.objects.exclude(feed__codename__in=EXCLUDED_FEEDS)  
site.register(FeedEntry, FeedEntryIndex)

#
# flatpages
#

class FlatPageIndex(indexes.SearchIndex):
    type = indexes.CharField(default='page')
    text = indexes.CharField(document=True, model_attr='content')
    title = indexes.CharField(model_attr='title') 
    link = indexes.CharField(model_attr='url') 
    def get_queryset(self):
        return FlatPage.objects.all()
site.register(FlatPage, FlatPageIndex)

#
# press
#

class PressArticleIndex(indexes.SearchIndex):
    type = indexes.CharField(default='press_article')
    text = indexes.CharField(document=True, model_attr='body')
    title = indexes.CharField(model_attr='headline') 
    link = indexes.CharField(model_attr='get_absolute_url')
    summary = indexes.CharField(model_attr='teaser') 
    def get_queryset(self):
        return PressArticle.objects.filter(is_public=True)
site.register(PressArticle, PressArticleIndex)

class PressReleaseIndex(indexes.SearchIndex):
    type = indexes.CharField(default='press_release')
    text = indexes.CharField(document=True, model_attr='body')
    title = indexes.CharField(model_attr='headline') 
    link = indexes.CharField(model_attr='get_absolute_url')
    summary = indexes.CharField(model_attr='teaser')     
    def get_queryset(self):
        return PressRelease.objects.filter(is_public=True)
site.register(PressRelease, PressReleaseIndex)