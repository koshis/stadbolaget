# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2020-03-07 18:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companyapp', '0003_auto_20200306_0719'),
    ]

    operations = [
        migrations.AddField(
            model_name='menucategory',
            name='Side Menu',
            field=models.BooleanField(default=True, help_text='if True page includes side menu'),
        ),
    ]