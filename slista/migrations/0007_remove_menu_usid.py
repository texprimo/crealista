# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slista', '0006_auto_20170426_2235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='usid',
        ),
    ]
