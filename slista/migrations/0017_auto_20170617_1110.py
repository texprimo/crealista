# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slista', '0016_auto_20170617_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='giorno',
            field=models.CharField(max_length=10, choices=[('Lunedì', 'lunedì'), ('Martedì', 'martedì'), ('Mercoledì', 'mercoledì'), ('Giovedì', 'giovedì'), ('Venerdì', 'venerdì'), ('Sabato', 'sabato'), ('Domenica', 'domenica')], blank=True, null=True),
        ),
    ]
