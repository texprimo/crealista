# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slista', '0005_auto_20170426_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='giorno',
            field=models.SmallIntegerField(choices=[(1, 'lunedì'), (2, 'martedì'), (3, 'mercoledì'), (4, 'giovedì'), (5, 'venerdì'), (6, 'sabato'), (7, 'domenica')]),
        ),
    ]
