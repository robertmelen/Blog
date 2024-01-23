from wagtail import blocks
from wagtail.templatetags.wagtailcore_tags import richtext
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock

class TitleAndTextBlock(blocks.StructBlock):
    """Title and text and nothing else."""

    title = blocks.CharBlock(required=True, help_text="Add your title")
    text = blocks.TextBlock(required=False, help_text="Add additional text")

    class Meta:  # noqa
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"

class ImageBlock(blocks.StructBlock):

     small_image = ImageChooserBlock(required=False, blank=True)
     medium_image = ImageChooserBlock(required=False, blank=True)
     large_image = ImageChooserBlock(required=False, blank=True)
     text = blocks.TextBlock(required=True, max_length=200)

     class Meta:  # noqa
        template = "streams/image_block.html"
        icon = "placeholder"
        label = "Image"

class WritingBlock(blocks.StructBlock):
        
        rich_text = blocks.RichTextBlock(required=False, max_length=2000, features=['h2', 'h3',  'h5', 
                                                                                    'h6', 'bold', 'italic', 'ol', 'ul',
                         'image', 'strikethrough', 'link', 'hr', 'code', 'document-link', 'blockquote'])

        class Meta:  # noqa
                template = "streams/richtext_block.html"
                icon = "placeholder"
                label = "Richtext"

    
class CodeBlock(blocks.StructBlock):

        CODE_CHOICES = [
                ('python', 'python'),
                ('javascript', 'javascript'),
                ('css', 'css'),
                ('html', 'html'),
               ('django', 'django'),
                ]


        
        language = blocks.ChoiceBlock(choices=CODE_CHOICES, default="language")
        text = blocks.TextBlock()

        class Meta:  # noqa
                template = "streams/code_block.html"
                icon = "placeholder"
                label = "Code"


class QuoteBlock(blocks.StructBlock):
      
      quote_text = blocks.TextBlock(required=False, max_length=2000)

      class Meta:  # noqa
                template = "streams/quote_block.html"
                icon = "placeholder"
                label = "Quote"
      
class GalleryBlock(blocks.StructBlock):
      
      gallery_images = blocks.ListBlock(ImageChooserBlock)
      gallery_heading = blocks.TextBlock(max_length=200)

      class Meta:  # noqa
                template = "streams/gallery_block.html"
                icon = "placeholder"
                label = "Gallery"

class EmbedBlock(blocks.StructBlock):
       
       embed = EmbedBlock()

       class Meta: 
                template = "streams/embed_block.html"
                icon = "placeholder"
                label = "Embed" 

     
class FullWidthImage(blocks.StructBlock):
       
        
        image = ImageChooserBlock(required=False, blank=True)
        text = blocks.TextBlock(required=True, max_length=200)
       
        class Meta:  # noqa
                template = "streams/full_width_image_block.html"
                icon = "placeholder"
                label = "Full width Image"    


class StravaBlock(blocks.StructBlock):

       code = blocks.TextBlock(required=True, max_length=50, help_text='''Please enter the code 
                               from data-embed-id= section of your Strava Embed code''') 

       class Meta:  # noqa
                template = "streams/strava_block.html"
                icon = "placeholder"
                label = "Embed Strava"

 
                
        
 