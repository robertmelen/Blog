from django import template
from home.models import Header, HomePage, Page

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