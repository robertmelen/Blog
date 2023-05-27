from wagtail import blocks
from wagtail.templatetags.wagtailcore_tags import richtext
from wagtail.images.blocks import ImageChooserBlock

class TitleAndTextBlock(blocks.StructBlock):
    """Title and text and nothing else."""

    title = blocks.CharBlock(required=True, help_text="Add your title")
    text = blocks.TextBlock(required=False, help_text="Add additional text")

    class Meta:  # noqa
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"

class ImageBlock(blocks.StructBlock):

     small_image = ImageChooserBlock(required=False, null=True, blank=True)
     medium_image = ImageChooserBlock(required=False, null=True, blank=True)
     large_image = ImageChooserBlock(required=False, null=True, blank=True)
     text = blocks.TextBlock(required=True, max_length=200)

     class Meta:  # noqa
        template = "streams/image_block.html"
        icon = "placeholder"
        label = "Image"

class WritingBlock(blocks.StructBlock):
        
        rich_text = blocks.RichTextBlock(required=False, max_length=2000)

        class Meta:  # noqa
                template = "streams/richtext_block.html"
                icon = "placeholder"
                label = "Richtext"

    
class CodeBlock(blocks.StructBlock):
        
        code_text = blocks.TextBlock(required=False, max_length=2000)

        class Meta:  # noqa
                template = "streams/code_block.html"
                icon = "placeholder"
                label = "Code"

             
             
             

 
                
        
 