# Generated by Django 4.2.2 on 2023-07-06 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_alter_subscription_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='subscription_status',
            field=models.BooleanField(default=False),
        ),
    ]
