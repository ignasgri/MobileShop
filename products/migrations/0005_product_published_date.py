# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-10 17:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20171210_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]