# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-12 16:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.CharField(max_length=100),
        ),
    ]
