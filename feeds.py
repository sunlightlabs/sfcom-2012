from django.contrib.syndication.views import Feed
from wordpress.models import Post

class BlogFeed(Feed):
    
    title = "Sunlight Foundation Blog"
    link = "http://sunlightfoundation.com/blog/"
    description = "Recent posts from the Sunlight Foundation blog"
    description_template = "feeds/blog_description.html"
        
    def items(self):
        return Post.objects.published().select_related()[:10]
        
    def item_link(self, item):
        return item.get_absolute_url()
        
    def item_author_name(self, item):
        return item.author.display_name
        
    def item_pubdate(self, item):
        return item.post_date
    
    def item_title(self, item):
        return item.title