# Generated by Django 4.2.2 on 2023-07-01 12:32

from django.db import migrations, models
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_alter_blog_short_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', froala_editor.fields.FroalaField()),
            ],
        ),
        migrations.CreateModel(
            name='Project_Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('client', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Project_Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='project/image/')),
            ],
        ),
    ]
