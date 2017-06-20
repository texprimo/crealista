# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slista', '0003_auto_20170425_1758'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='composizione',
            name='quantitaP',
        ),
        migrations.AddField(
            model_name='composizione',
            name='UnMisIngr',
            field=models.ForeignKey(default=1, to='slista.UM', related_name='usata_in'),
            preserve_default=False,
        ),
    ]
