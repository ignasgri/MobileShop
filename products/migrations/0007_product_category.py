# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-20 20:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_remove_category_products'),
        ('products', '0006_product_condition'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(to='categories.Category'),
        ),
    ]