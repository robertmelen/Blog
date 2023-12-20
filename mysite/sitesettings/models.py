from django.db import models

from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from modelcluster.fields import ParentalKey
from wagtail.models import Orderable, ClusterableModel



@register_setting(icon='placeholder')

class privacy_notice(BaseSiteSetting):
    notice = RichTextField(default="privacy")

class Meta:
        verbose_name = 'Privacy notice'

panels =  [
    FieldPanel('notice'),
]


@register_setting(icon='placeholder')

class copyright_notice(BaseSiteSetting):
    copyright_info = RichTextField(default="copyright")

class Meta:
        verbose_name = 'Copyright notice'

panels =  [
    FieldPanel('copyright_info'),
]




@register_setting
class FooterSettings(BaseSiteSetting, ClusterableModel):
    footer_messages = models.BooleanField("Add modal popups to footer?", default=True, help_text='Untick to hide')
    panels = [
       
            FieldPanel('footer_messages'),
            InlinePanel('notices')
            ]
    
          
class FooterNotices(Orderable):
      settings_page = ParentalKey(FooterSettings, related_name="notices", null=True) 
      title = models.CharField(max_length=200, blank=True, null=True)
      text = RichTextField()

      panels =  [
    FieldPanel('title'),
    FieldPanel('text'),
]
        
@register_setting    
class ContactInfo(BaseSiteSetting):
      text = RichTextField()

      FieldPanel('text'),

@register_setting    
class DataWarning(BaseSiteSetting):
      message = models.CharField(max_length=300, blank=True)
      policy = RichTextField() 
      FieldPanel('message'),
      FieldPanel('policy'),  




