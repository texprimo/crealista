# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slista', '0008_auto_20170426_2258'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='composizione',
            options={'verbose_name_plural': 'Voci'},
        ),
        migrations.AlterModelOptions(
            name='um',
            options={'verbose_name_plural': 'Uni_di_misura'},
        ),
        migrations.AddField(
            model_name='vocep',
            name='usid',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='menu',
            name='utente',
            field=models.ForeignKey(blank=True, to='slista.Utente', null=True),
        ),
    ]
