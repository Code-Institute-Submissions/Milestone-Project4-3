# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-05-10 17:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('city', models.CharField(blank=True, default='', max_length=100)),
                ('website', models.URLField(blank=True, default='')),
                ('phone', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('image', models.ImageField(blank=True, upload_to='avatars/%Y/%m/%d')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
