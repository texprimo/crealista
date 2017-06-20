# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slista', '0013_remove_utente_usid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vocep',
            name='proprietario',
        ),
        migrations.RemoveField(
            model_name='vocep',
            name='voce_ptr',
        ),
        migrations.AlterModelOptions(
            name='utente',
            options={'verbose_name_plural': 'Utenti'},
        ),
        migrations.RemoveField(
            model_name='menu',
            name='usid',
        ),
        migrations.AddField(
            model_name='voce',
            name='proprietario',
            field=models.ForeignKey(blank=True, null=True, to='slista.Utente'),
        ),
        migrations.DeleteModel(
            name='VoceP',
        ),
    ]
