from django.shortcuts import render_to_response
from django.template import RequestContext
from sunlightfoundation.com.models import FeaturedPost

def index(request):
    
    featured_posts = FeaturedPost.objects.filter(published=True).order_by("-date_published")[:2]
    
    data = {
        'featured_posts': featured_posts,
    }
    
    return render_to_response('index.html', data, context_instance=RequestContext(request))