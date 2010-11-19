from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from postmark import PMMail
from sunlightfoundation.com.forms import ContactForm
from sunlightfoundation.com.models import FeaturedPost, FeaturedTopic

def index(request):
    
    if 'message' in request.GET:
        msg = request.GET['message']
        messages.debug(request, msg)
        messages.info(request, msg)
        messages.success(request, msg)
        messages.warning(request, msg)
        messages.error(request, msg)
    
    featured_posts = FeaturedPost.objects.filter(published=True).order_by("-date_published")[:2]
    featured_topics = FeaturedTopic.objects.filter(published=True).order_by('-id')[:3]
    
    data = {
        'featured_posts': featured_posts,
        'featured_topics': featured_topics,
    }
    
    return render_to_response('index.html', data, context_instance=RequestContext(request))


def contact(request):
    
    if request.method == "POST":
        
        form = ContactForm(request.POST)
        
        if form.is_valid():
            
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['from_email']
            message = "%s <%s> wrote:\n\n%s" % (name, from_email, form.cleaned_data['message'])
            
            PMMail(
                to='contact@sunlightfoundation.com',
                reply_to="%s <%s>" % (name, from_email),
                subject="[SunlightFoundation.com] message from %s" % name,
                text_body=message,
            ).send()
            
            messages.success(request, 'Thank you for contacting us! We will get back to you shortly.')
            return HttpResponseRedirect("/contact/")
            
    else:
        
        form = ContactForm()
        
    return render_to_response("contact/form.html",
                              { "form": form },
                              context_instance=RequestContext(request))

def projects(request):
    return render_to_response("projects/index.html",
                              context_instance=RequestContext(request))