# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-29 13:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='bid_expiry_date',
        ),
    ]