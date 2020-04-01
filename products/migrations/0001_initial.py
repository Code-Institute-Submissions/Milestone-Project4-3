# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-29 13:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=254)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=3, max_digits=10)),
                ('bid_price', models.DecimalField(decimal_places=3, max_digits=10)),
                ('author', models.CharField(default='', max_length=254)),
                ('date_made', models.CharField(default='', max_length=254)),
                ('country_made_in', models.CharField(default='', max_length=254)),
                ('height', models.DecimalField(decimal_places=1, max_digits=5)),
                ('width', models.DecimalField(decimal_places=1, max_digits=5)),
                ('past_owners', models.TextField()),
                ('date_created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('bid_expiry_date', models.DateTimeField(blank=True, null=True)),
                ('main_image', models.ImageField(upload_to='images/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='ProductsPictures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/%Y/%m/%d')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
        ),
    ]