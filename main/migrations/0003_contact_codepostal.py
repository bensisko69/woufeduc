# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-18 21:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='codePostal',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
