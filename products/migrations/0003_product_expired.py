# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-05-14 14:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_product_current_b'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='expired',
            field=models.BooleanField(default=False),
        ),
    ]