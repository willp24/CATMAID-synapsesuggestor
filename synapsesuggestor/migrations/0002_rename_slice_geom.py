# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-03 18:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('synapsesuggestor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='synapseslice',
            old_name='convex_hull_2d',
            new_name='geom_2d',
        ),
    ]
