# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-29 18:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyBlog', '0004_auto_20170414_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft..'), ('published', 'Published..')], default='draft', max_length=10),
        ),
    ]