# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slista', '0014_auto_20170616_1947'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trasformatore',
            options={'verbose_name_plural': 'Trasformazioni'},
        ),
        migrations.AlterField(
            model_name='trasformatore',
            name='UMEntrata',
            field=models.ForeignKey(to='slista.UM', related_name='da'),
        ),
        migrations.AlterField(
            model_name='trasformatore',
            name='UMUscita',
            field=models.ForeignKey(to='slista.UM', related_name='a'),
        ),
        migrations.AlterField(
            model_name='um',
            name='corrisponde',
            field=models.ManyToManyField(to='slista.UM', through='slista.Trasformatore', related_name='va_in'),
        ),
    ]
