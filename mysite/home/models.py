from django.db import models
from PIL import Image as PILImage
from django.utils import timezone
from mysite.settings.base import live_deploy



# New imports added for ParentalKey, Orderable, InlinePanel
from blog.models import BlogListingPage

from modelcluster.fields import ParentalKey
from wagtail.admin.panels import TabbedInterface, ObjectList

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel, FieldRowPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet

from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.contrib.forms.panels import FormSubmissionsPanel



from wagtail.images.blocks import ImageChooserBlock
from wagtail import blocks
from wagtail.fields import StreamField
from wagtail.blocks import RichTextBlock
from wagtail.contrib.search_promotions.models import Query

from django.http import HttpResponse
from django.shortcuts import render
from wagtail.contrib.routable_page.models import RoutablePageMixin, path


from blog.models import BlogDetailPage
from django_htmx.http import push_url
from wagtail.contrib.routable_page.models import RoutablePageMixin, path, re_path

from wagtail.images.models import Image, AbstractImage, AbstractRendition
from wagtailmetadata.models import MetadataPageMixin

import math
from fractions import Fraction
from io import BytesIO
import io

from django.views.generic import TemplateView
from wagtail.models import Site



class FormField(AbstractFormField):
    page = ParentalKey('FormPage', on_delete=models.CASCADE, related_name='form_fields')


class FormPage(AbstractEmailForm):
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FormSubmissionsPanel(),
        FieldPanel('intro'),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]

    

    def serve(self, request, *args, **kwargs):

        if live_deploy is True:
            get_ip_address(request)
        
        #THIS WAS TO TEST COOKIES IN VIEWS BUT WASN'NEEDED AS
        #TEMPLATE CONDITIONAL DID THE JOB. I'll keep this here for 
        #reference.
        # value = request.COOKIES.get('declined')
        # if value:
        #     print("contact declined") 
        #     message = "sorry not available due to declining cookies, please refresh the page"
        #     return HttpResponse(message)
        # else: 
        return super().serve(request)
              
def get_ip_address(request):
            
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            time_stamp = timezone.now()
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]
            else:
                ip = request.META.get('REMOTE_ADDR')
            id = request.COOKIES.get('visitor_id')
            with open(r'/file/ip_logs.txt', 'a') as file:
                    file.write('message' + " " + ip + " " + str(time_stamp) + "" + str(id) + '\n')
            return ip
              



  

def apex_to_shutter_speed(apex_value):
    # Calculate the shutter speed in seconds
    shutter_speed_seconds = math.pow(2, -apex_value)
    return shutter_speed_seconds

def convert_to_standard_shutter_speed(seconds):
     # Calculate the reciprocal of the shutter speed in seconds
    reciprocal = 1 / seconds
    
    # Define a list of common denominators for standard shutter speeds
    common_denominators = [1, 2, 4, 8, 15, 30, 60, 125, 250, 500, 1000]
    
    # Find the closest denominator from the list
    closest_denominator = min(common_denominators, key=lambda x: abs(reciprocal - round(reciprocal * x) / x))
    
    # Calculate the standard shutter speed fraction
    standard_shutter_speed = Fraction(round(reciprocal * closest_denominator), closest_denominator)

    return standard_shutter_speed
    
    



class CustomImage(AbstractImage):
    caption = models.CharField(max_length=1000, blank=True)
    location = models.CharField(max_length=100, blank=True)
    date = models.CharField(max_length=100, blank=True)
    camera = models.CharField(max_length=255, blank=True)
    copyright = models.CharField(max_length=200, blank=True)
    shutter = models.CharField(max_length=100, blank=True)
    aperture = models.CharField(max_length=100, blank=True)

    admin_form_fields = Image.admin_form_fields + (
       'caption', 'location', 'date', 'camera', 'copyright', 'shutter', 'aperture'
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.file:
            image_file = BytesIO(self.file.read())
            with PILImage.open(image_file) as img:
               exif_data = img._getexif()
               if exif_data:
                    image_description = exif_data.get(270, '') 
                    camera_model = exif_data.get(272, '') 
                    copyright = exif_data.get(33432, '')
                    shutter = exif_data.get(37377, '')
                    aperture = exif_data.get(37378, '')
                    if not self.caption:
                        self.caption = image_description
                    if not self.camera:
                        self.camera = camera_model
                    if not self.copyright:
                        self.copyright = copyright
                    if not self.shutter:
                        apex_value = float(shutter)
                        shutter_speed_seconds = apex_to_shutter_speed(apex_value)
                        standard_shutter_speed = convert_to_standard_shutter_speed(shutter_speed_seconds)
                        self.shutter = standard_shutter_speed 
                    if not self.aperture:
                        self.aperture = aperture
            super().save(*args, **kwargs)

   

class CustomRendition(AbstractRendition):
    image = models.ForeignKey(CustomImage, on_delete=models.CASCADE, related_name='renditions')

    class Meta:
        unique_together = (
            ('image', 'filter_spec', 'focal_point_key'),
        )

 




class HeroBlock(blocks.StructBlock):
    Title = blocks.CharBlock()
    image =  ImageChooserBlock()
    text = blocks.CharBlock()
    about = blocks.TextBlock()
    about_image = ImageChooserBlock()
   


class HomePage(MetadataPageMixin, RoutablePageMixin, Page):
    home_header = models.ForeignKey('home.Header', null=True,
          blank=True,
          on_delete=models.SET_NULL,
          related_name='+')
    page_title = RichTextField(blank=True)
    body = RichTextField(blank=True)
    date = models.DateField("Post date")
    hero = StreamField([
        ('hero', HeroBlock()),
    ],  use_json_field=True, null=True)
    gallery_image = models.ForeignKey(
        CustomImage,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    
   

    content_panels = Page.content_panels + [
        FieldPanel('home_header'),
        FieldPanel('page_title'),
        FieldPanel('body'),
        FieldPanel('date'),
        FieldPanel('hero'),
        FieldPanel('gallery_image'),
       
        
        
    ]

    subpage_types = ['blog.BlogListingPage', 'home.Terms', 'home.FormPage']


  

    def get_recent_blogs(self):
        max_count = 4 # max count for displaying post
        return  BlogDetailPage.objects.all().order_by('-first_published_at')[:max_count]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['menu_objects'] = BlogListingPage.objects.live().child_of(self)
        context['recent_posts'] = self.get_recent_blogs()
        context['id'] = request.COOKIES.get('visitor_id') 
        
        
      
        return context
    
   

    @path('blog-search/')
    def blog_search(self, request,):
        if request.htmx:
            if request.method == 'GET':
                return self.render(
                        request,
                        context_overrides={
                            'test': "test"
                            },
                        template = "home/search.html",
                    )
            if request.method == 'POST':
                    search_query = request.POST.get('search-input')
                    search_results = BlogDetailPage.objects.all().autocomplete(search_query)
                    return self.render(
                            request,
                            context_overrides={
                                'search_query': search_query,
                                'search_results': search_results,
                                },
                            template = "home/search-results.html",
                        )
                
        
    @path('bio/')
    def blog_bio(self, request,):
     
      return self.render(
            request,
            context_overrides={
                'test': "test"
                },
            template = "partials/bio.html",
        )
    

    @path('contact/')
    def blog_contact(self, request):
        if request.POST:
            message = "Contact form"
            
            return self.render(
                    request,
                    context_overrides={
                        'test': "test"
                        },
                    template = "home/contact.html",
                )
    
   
    def serve(self, request, *args, **kwargs):
        # Call the middleware to set the session variable
        super().serve(request, *args, **kwargs)

        if request.session.get('needs_cookie', False):
            # Set the cookie if the needs_cookie session variable is True
            response = super().serve(request, *args, **kwargs)
            response.set_cookie('visitor_id', request.visitor_id)
            request.session['needs_cookie'] = False  # Reset the session variable
            return response
        
        if request.htmx:
            if request.htmx.trigger == "accept":
                response = HttpResponse()
                response.set_cookie('accepted', True)
                return response
            if request.htmx.trigger == "decline":
                response = HttpResponse()
                response.set_cookie('declined', True)
                return response
            
      
        return super().serve(request, *args, **kwargs)
                
                    


                
                
        
    
    # def serve(self, request, *args, **kwargs):
    #         if request.htmx:
    #             if request.GET.get('bio'):
    #                 context = super().get_context(request, *args, **kwargs)
    #                 print("debug htmx")
    #                 return render(request, "partials/bio.html", context)
            
    #         print("debug normal")
        
            
        
    #         return super().serve(request)
                





#snippets    

@register_snippet
class Header(models.Model):
    logo = models.ForeignKey(
        CustomImage,
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
        CustomImage,
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
    

@register_snippet
class Gallery(models.Model):
    images = models.ForeignKey(
        CustomImage,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    title = models.CharField(max_length=500, null=True, blank=True)
    caption = models.CharField(max_length=500, null=True, blank=True )
    


   
    

    panels = [
        FieldPanel('images'),
        FieldPanel('title'),
        FieldPanel('caption'),
        
       
    ]

    class Meta:
        verbose_name = "Gallery Image"

    def __str__(self):
        return self.images.title
        


class Terms(Page):
    text = RichTextField(blank=True, null=True)
    created = models.DateField('Date', blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('text'),
        
    ]
   
    page_description = "Use this for Terms and Conditions"

    def __str__(self):
        return "this is a test"
        

    
    # def serve(self, request, *args, **kwargs):
    #     if request.htmx:
    #         print("HTMX true")
           
    #         context = super().get_context(request, *args, **kwargs)
    #         return render(request, "partials/terms.html", context)
    
    #     return super().serve(request)
    


class RobotsView(TemplateView):

    content_type = 'text/plain'
    template_name = 'home/robots.txt'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        request = context['view'].request
        context['wagtail_site'] = Site.find_for_request(request)
        return context