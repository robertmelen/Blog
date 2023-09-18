# Generated by Django 4.1.8 on 2023-09-17 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
        ('home', '0028_remove_gallery_background_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='gallery_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]
