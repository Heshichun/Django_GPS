# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-08 11:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('addresstest', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='address_info',
        ),
    ]
