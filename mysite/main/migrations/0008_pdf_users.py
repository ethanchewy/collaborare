# Generated by Django 3.0.4 on 2020-03-08 10:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0007_auto_20200308_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdf',
            name='users',
            field=models.ManyToManyField(related_name='pdf_users', to=settings.AUTH_USER_MODEL),
        ),
    ]
