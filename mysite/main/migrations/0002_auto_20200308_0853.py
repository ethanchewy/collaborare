# Generated by Django 3.0.4 on 2020-03-08 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='related_concept',
            field=models.TextField(default='Nothing'),
        ),
        migrations.AddField(
            model_name='comment',
            name='x',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='y',
            field=models.IntegerField(default=0),
        ),
    ]
