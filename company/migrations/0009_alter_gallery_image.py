# Generated by Django 4.2.2 on 2023-07-17 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0008_alter_blog_image_alter_gallery_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.URLField(),
        ),
    ]