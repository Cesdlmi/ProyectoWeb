# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-21 05:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0005_alumno_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumno',
            name='Usuario',
        ),
    ]