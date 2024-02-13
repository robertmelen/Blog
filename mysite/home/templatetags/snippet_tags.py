from django import template
import re
from home.models import Header, HomePage, Page, Gallery, BlogListingPage
from django.utils import timezone

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
    


@register.simple_tag(takes_context=True)
def is_homepage(context):
    
    if context.request.path == "/":
        print(context.request.path)
        return "homepage"


@register.filter(name="cut")
def cut(value, arg):
    return value.replace(arg, " ")



@register.filter(name="time_posted")
def time_posted(value):
    if value.first_published_at:
        delta = timezone.now() - value.first_published_at
        return delta.days
    return None



@register.filter
def get_first_text_body(blocks):
    for block in blocks:
        if block.block_type == 'text_body':
            return block.value.get('rich_text', '')
    return ''





@register.filter(name='render_head_tags')
def render_head_tags(tags):
    keyword_list = [tag.name for tag in tags]
    keywords_string = ', '.join(keyword_list)
    return f'<meta name="keywords" content="{keywords_string}">'




