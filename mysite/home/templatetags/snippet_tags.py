from django import template
import re
from home.models import Header, HomePage, Page, Gallery

register = template.Library()


@register.inclusion_tag('snippets/header.html', takes_context=True)
def headers(context):
    return {
        'home_page_objects': HomePage.objects.all(),
        
        
        'request': context['request'],
    }





@register.inclusion_tag('snippets/breadcrumbs.html', takes_context=True)
def breadcrumbs(context):
    self = context.get('self')
    if self is None or self.depth <= 2:
        # When on the home page, displaying breadcrumbs is irrelevant.
        ancestors = ()
    else:
        ancestors = Page.objects.ancestor_of(
            self, inclusive=True).filter(depth__gt=1)
    return {
        'ancestors': ancestors,
        'request': context['request'],
    }


@register.inclusion_tag('snippets/gallery.html', takes_context=True)
def gallery(context):
    return {
        'gallery': Gallery.objects.all(),
        'request': context['request'],}








@register.filter(name="embedurl")
def get_embed_url_with_parameters(url):
    if "youtube.com" in url or "youtu.be" in url:
        regex = r"(?:https:\/\/)?(?:www\.)?(?:youtube\.com|youtu\.be)\/(?:watch\?v=)?(.+)"  # Get video id from URL
        embed_url = re.sub(
            regex, r"https://www.youtube.com/embed/\1", url
        )  # Append video id to desired URL
        print(embed_url)
        embed_url_with_parameters = embed_url + "?rel=0"  # Add additional parameters
        return embed_url_with_parameters
    else:
        return None