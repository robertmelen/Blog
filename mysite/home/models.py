from django.db import models

# New imports added for ParentalKey, Orderable, InlinePanel
from blog.models import BlogListingPage

from modelcluster.fields import ParentalKey

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet


from wagtail.images.blocks import ImageChooserBlock
from wagtail import blocks
from wagtail.fields import StreamField
from wagtail.blocks import RichTextBlock

from django.http import HttpResponse
from django.shortcuts import render
from wagtail.contrib.routable_page.models import RoutablePageMixin, path


from blog.models import BlogDetailPage
from django_htmx.http import push_url
from wagtail.contrib.routable_page.models import RoutablePageMixin, path


class HeroBlock(blocks.StructBlock):
    Title = blocks.CharBlock()
    image =  ImageChooserBlock()
    text = blocks.CharBlock()
   


class HomePage(Page):
    home_header = models.ForeignKey('home.Header', null=True,
          blank=True,
          on_delete=models.SET_NULL,
          related_name='+')
    page_title = RichTextField(blank=True)
    body = RichTextField(blank=True)
    date = models.DateField("Post date")
    hero = StreamField([
        ('hero', HeroBlock()),
    ], use_json_field=True, max_num = 1)

   

    content_panels = Page.content_panels + [
        FieldPanel('home_header'),
        FieldPanel('page_title'),
        FieldPanel('body'),
        FieldPanel('date'),
        FieldPanel('hero'),
       
        
        
    ]

    subpage_types = ['blog.BlogListingPage']

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['menu_objects'] = BlogListingPage.objects.live().child_of(self)
        print(context)
        return context



        # Add extra variables and return the updated context
       

    # #checking fot htmx request working
    # def serve(self, request):
    #     if request.htmx:
    #         print("yes")
    #     return super().serve(request)

   
               
#orderables 




#snippets    

@register_snippet
class Header(models.Model):
    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    
    text = models.CharField(max_length=255)

    panels = [
        MultiFieldPanel([
        FieldPanel('logo'),
        FieldPanel('text'),])
    ]

    def __str__(self):
        return self.text
    







@register_snippet
class Header_Photo(models.Model):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    
    

    panels = [
        FieldPanel('image'),
       
    ]

    def __str__(self):
        return self.image.title
    

