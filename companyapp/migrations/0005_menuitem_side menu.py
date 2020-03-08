# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2020-03-07 19:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companyapp', '0004_menucategory_side menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='Side Menu',
            field=models.BooleanField(default=True, help_text='if True page includes side menu'),
        ),
    ]
