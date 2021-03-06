# Generated by Django 3.0.4 on 2020-03-08 09:04

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200308_0859'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='parent_thread_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_thread_id', to='main.Thread'),
        ),
    ]
