from django.shortcuts import render_to_response
from django.template import RequestContext
from sunlightfoundation.com.models import FeaturedPost, FeaturedTopic

def index(request):
    
    featured_posts = FeaturedPost.objects.filter(published=True).order_by("-date_published")[:2]
    featured_topics = FeaturedTopic.objects.filter(published=True).order_by('-id')[:3]
    
    data = {
        'featured_posts': featured_posts,
        'featured_topics': featured_topics,
    }
    
    return render_to_response('index.html', data, context_instance=RequestContext(request))