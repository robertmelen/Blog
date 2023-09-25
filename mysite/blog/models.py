from django.db import models
from django import forms
from taggit.models import TaggedItemBase
from modelcluster.contrib.taggit import ClusterTaggableManager
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from readtime import of_html, of_markdown, of_text



from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.fields import StreamField
from wagtail.models import Page, Orderable
from wagtail.images.blocks import ImageChooserBlock 
from django.shortcuts import render
from wagtail.snippets.models import register_snippet
from wagtail import blocks
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.models import ClusterableModel



from blog import blocks as my_blocks

from wagtail.contrib.routable_page.models import RoutablePageMixin, path, route, re_path

from django.http import HttpResponse

from django.utils.text import slugify

from wagtail_icon_picker.fields import IconField
from wagtail_icon_picker.edit_handlers import IcofontIconPickerPanel, BoxiconsPickerPanel




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



class BlogAuthor(ClusterableModel):
    name = models.CharField(max_length=200)
    bio = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    image = models.ForeignKey(
        ('home.CustomImage'),
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
    ),
    
    InlinePanel('author_socials', label="Socials"),

]
    
    def __str__(self):
        return self.name
    
    class Meta:  
        verbose_name = "Blog Author"
        verbose_name_plural = "Blog Authors"

register_snippet(BlogAuthor)


SOCIAL_CHOICES = (
    ("Facebook", "Facebook"),
    ("Twitter", "Twitter"),
    ("Github", "Github"),

   )

class AuthorSocials(Orderable):
    page = ParentalKey("blog.BlogAuthor", on_delete=models.CASCADE, related_name='author_socials')
    network = models.CharField(max_length = 20, choices = SOCIAL_CHOICES, default="Facebook")
    url = models.URLField()

    panels = [
       
        FieldPanel('url'),
        FieldPanel('network'),
        

       
        
    ]
    

    

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
        
    
    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        context["posts"] = BlogDetailPage.objects.live().public().order_by('-first_published_at')
        
        paginator = Paginator(context["posts"], 4)
        page = request.GET.get("page")
        try:
           posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
           posts = paginator.page(paginator.num_pages)
        context["posts"] = posts
        return context


    @re_path(r'^tagged/(\w+)/$')
    def post_by_tag(self, request, tag, *args, **kwargs):
        all_post = BlogDetailPage.objects.all()
        context = all_post.filter(tags__name=tag)
        print(context)   
        return self.render(request, template="partials/blog_by_tag.html", context_overrides = {'posts': context, 'tagged':tag})  
   

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
        ('home.CustomImage'),
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