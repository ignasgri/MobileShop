# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-10 17:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_published_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='condition',
            field=models.CharField(choices=[('New', 'New'), ('Used', 'Used')], default='New', max_length=4),
        ),
    ]
