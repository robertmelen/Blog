from django.db import models
from django import forms
from taggit.models import TaggedItemBase
from modelcluster.contrib.taggit import ClusterTaggableManager
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator



from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.fields import StreamField
from wagtail.models import Page, Orderable
from wagtail.images.blocks import ImageChooserBlock 
from django.shortcuts import render
from wagtail.snippets.models import register_snippet
from wagtail import blocks
from modelcluster.fields import ParentalKey, ParentalManyToManyField



from blog import blocks as my_blocks

from wagtail.contrib.routable_page.models import RoutablePageMixin, path, route

from django.http import HttpResponse

from django.utils.text import slugify



class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'BlogDetailPage',
        related_name='tagged_items',
        on_delete=models.CASCADE,
    )



class BlogAuthorsOrderable(Orderable):
     page = ParentalKey("blog.BlogDetailPage", related_name="blog_authors")
     author = models.ForeignKey(
        "blog.BlogAuthor",
        on_delete=models.CASCADE,
    )

     panels = [
        FieldPanel("author"),
    ]



class BlogAuthor(models.Model):
    name = models.CharField(max_length=200)
    bio = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="+",
    )
    facebook = models.CharField(max_length=200, blank=True, null=True)
    twitter = models.CharField(max_length=200, blank=True, null=True)
    instagram = models.CharField(max_length=200, blank=True, null=True)
    
    panels = [
    MultiFieldPanel(
        [
            FieldPanel("name"),
            FieldPanel("image"),
            FieldPanel("bio"),
        ],
        heading="Name, Image and Bio",
    ),
    MultiFieldPanel(
        [
            FieldPanel("facebook"),
            FieldPanel("twitter"),
            FieldPanel("instagram"),
        ],
        heading="Social"
    )
]
    
    def __str__(self):
        return self.name
    
    class Meta:  
        verbose_name = "Blog Author"
        verbose_name_plural = "Blog Authors"

register_snippet(BlogAuthor)






class BlogListingPage(RoutablePageMixin, Page):
    """Listing page lists all the Blog Detail Pages."""

    
    custom_title = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        help_text='Overwrites the default title',
    )

    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
    ]

    def get_template(self, request, *args, **kwargs):
        if request.htmx and request.GET.get('elements'):
             return 'partials/blog_list_element.html'
        else:
            return 'blog/blog_listing_page.html'
        
    def get_posts(self):
        return BlogListingPage.objects.descendant_of(self).live()
        
    @route(r'^tag/(?P<tag>[-\w]+)/$')
    def post_by_tag(self, request, tag, *args, **kwargs):
        self.posts = self.get_posts().filter(tags__slug=tag)
        return self.render(request)





    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        context["posts"] = BlogDetailPage.objects.live().public().order_by('-first_published_at')

        
    
      
            
        
      
        
        paginator = Paginator(context["posts"], 2)
       
        page = request.GET.get("page")
        try:
           
            posts = paginator.page(page)
            
        except PageNotAnInteger:
            
            posts = paginator.page(1)
        except EmptyPage:
           
            posts = paginator.page(paginator.num_pages)


        if request.GET.get('tag', None):
            tags = request.GET.get('tag')
            posts = posts.filter(tags__slug__in=[tags]) 

       

       
       



       
    
        
      
        context["posts"] = posts
        return context
    
  
                

        
          
        
        
    def get_paginated_posts(self, request, qs):
        # https://docs.djangoproject.com/en/4.0/topics/pagination/#using-paginator-in-a-view-function
        paginator = Paginator(qs, 2)
        page = request.GET.get("page")
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.object_list.none()

        return posts

        




class BlogDetailPage(Page):
    """Blog detail page."""

    custom_title = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        help_text='Overwrites the default title',
    )
    blog_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )

    categories = ParentalManyToManyField('blog.BlogCategories', blank=True)
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    summary = models.CharField(max_length=100, blank=True, null=True)

    content = StreamField(
        [
            
            ("title_and_text", my_blocks.TitleAndTextBlock()),
            ("image", my_blocks.ImageBlock()),
            ("text_body", my_blocks.WritingBlock()),
            ('gallery', my_blocks.GalleryBlock()),
            ('code', my_blocks.CodeBlock()),
            ('quote', my_blocks.QuoteBlock()),
            ('embed', my_blocks.EmbedBlock()),
          
          
           
        ],
        use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
        FieldPanel("summary"),
        FieldPanel("blog_image"),
        FieldPanel("content"),
        FieldPanel("tags"),
        FieldPanel("categories", widget=forms.CheckboxSelectMultiple),
        
         MultiFieldPanel(
            [
                InlinePanel("blog_authors", label="Author", min_num=1, max_num=4)
                
            ],
            heading="Author(s)"
        ),

        
    ]

    @property
    def next_post(self):
        return self.get_next_sibling()
        
       
        
    
    @property
    def previous_post(self):
        return self.get_prev_sibling()
    
    # @property
    # def summary(self):
    #     split = self.
    #     return self.get_prev_sibling()
        


    def __str__(self):
        return self.custom_title
    
    


@register_snippet
class BlogCategories(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    icon = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('icon'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'blog categories'