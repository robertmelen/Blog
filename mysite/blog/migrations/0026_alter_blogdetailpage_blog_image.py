# Generated by Django 4.1.8 on 2023-09-24 23:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0038_customimage_shutter'),
        ('blog', '0025_alter_blogauthor_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogdetailpage',
            name='blog_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='home.customimage'),
        ),
    ]
