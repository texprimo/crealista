# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slista', '0017_auto_20170617_1110'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='voce',
            options={'ordering': ['nome'], 'verbose_name_plural': 'Voci'},
        ),
        migrations.AddField(
            model_name='voce',
            name='genere',
            field=models.CharField(null=True, max_length=40, blank=True),
        ),
        migrations.AddField(
            model_name='voce',
            name='tipo',
            field=models.CharField(null=True, max_length=40, blank=True),
        ),
        migrations.AlterField(
            model_name='composizione',
            name='prodotto',
            field=models.ForeignKey(to='slista.Voce', related_name='componenti'),
        ),
        migrations.AlterField(
            model_name='dettaglio',
            name='lista',
            field=models.ForeignKey(to='slista.Lista', related_name='r_dettaglio'),
        ),
        migrations.AlterField(
            model_name='trasformatore',
            name='UMEntrata',
            field=models.ForeignKey(to='slista.UM', related_name='a'),
        ),
        migrations.AlterField(
            model_name='trasformatore',
            name='UMUscita',
            field=models.ForeignKey(to='slista.UM', related_name='da'),
        ),
        migrations.AlterField(
            model_name='um',
            name='corrisponde',
            field=models.ManyToManyField(related_name='viene_da', to='slista.UM', through='slista.Trasformatore'),
        ),
    ]
