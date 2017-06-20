# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slista', '0004_auto_20170425_1803'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={'verbose_name_plural': 'Menù'},
        ),
        migrations.AlterModelOptions(
            name='voce',
            options={'verbose_name_plural': 'Voci'},
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='utentek',
            new_name='utente',
        ),
        migrations.AddField(
            model_name='menu',
            name='usid',
            field=models.SmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='menu',
            name='giorno',
            field=models.SmallIntegerField(choices=[(1, 'lunedì'), (2, 'martedì')]),
        ),
    ]
