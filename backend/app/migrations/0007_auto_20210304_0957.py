# Generated by Django 3.1.7 on 2021-03-04 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20210304_0952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audio',
            name='title',
        ),
        migrations.RemoveField(
            model_name='text',
            name='title',
        ),
        migrations.RemoveField(
            model_name='video',
            name='title',
        ),
    ]
