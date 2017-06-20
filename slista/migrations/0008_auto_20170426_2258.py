# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slista', '0007_remove_menu_usid'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='usid',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='utente',
            name='usid',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
