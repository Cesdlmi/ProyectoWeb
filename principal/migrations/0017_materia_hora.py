# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-22 23:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0016_auto_20180522_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='materia',
            name='Hora',
            field=models.CharField(default=0, max_length=15),
            preserve_default=False,
        ),
    ]
