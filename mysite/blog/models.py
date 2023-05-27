from django.db import models


from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.fields import StreamField
from wagtail.models import Page, Orderable
from wagtail.images.blocks import ImageChooserBlock 
from django.shortcuts import render
from wagtail.snippets.models import register_snippet
from wagtail import blocks
from modelcluster.fields import ParentalKey


from blog import blocks as my_blocks

from wagtail.contrib.routable_page.models import RoutablePageMixin, path

from django.http import HttpResponse

from django.utils.text import slugify



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






class BlogListingPage(Page):
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

   

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        context["posts"] = BlogDetailPage.objects.live().public()
        return context




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

    content = StreamField(
        [
            
            ("title_and_text", my_blocks.TitleAndTextBlock()),
            ("image", my_blocks.ImageBlock()),
            ("text_body", my_blocks.WritingBlock()),
            ('gallery', blocks.ListBlock(ImageChooserBlock())),
            ('code', my_blocks.CodeBlock())
          
          
           
        ],
        use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
        FieldPanel("blog_image"),
        FieldPanel("content"),
         MultiFieldPanel(
            [
                InlinePanel("blog_authors", label="Author", min_num=1, max_num=4)
            ],
            heading="Author(s)"
        ),
    ]


    def __str__(self):
        return self.custom_title
