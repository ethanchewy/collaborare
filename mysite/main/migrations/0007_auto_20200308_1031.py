# Generated by Django 3.0.4 on 2020-03-08 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200308_0904'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdf',
            name='images_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pdf',
            name='url_path',
            field=models.TextField(default='Nothing'),
        ),
    ]
