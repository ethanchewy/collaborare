# Generated by Django 3.0.4 on 2020-03-08 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200308_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='pdf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.PDF'),
        ),
    ]