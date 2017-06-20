# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slista', '0015_auto_20170617_1005'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dettaglio',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('prezzo', models.FloatField()),
                ('stato', models.CharField(max_length=100)),
                ('quantità', models.FloatField()),
                ('UMisura', models.CharField(max_length=20)),
                ('Tot_riga', models.FloatField()),
                ('articolo', models.ForeignKey(to='slista.Voce')),
            ],
            options={
                'verbose_name_plural': 'Righe Lista',
            },
        ),
        migrations.CreateModel(
            name='Lista',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('data', models.DateField(blank=True, null=True)),
                ('stato', models.CharField(max_length=20)),
                ('fornitore', models.CharField(max_length=100)),
                ('utente', models.ForeignKey(to='slista.Utente')),
            ],
            options={
                'verbose_name_plural': 'Liste',
            },
        ),
        migrations.AlterModelOptions(
            name='composizione',
            options={'verbose_name_plural': 'Ingredienti'},
        ),
        migrations.AlterModelOptions(
            name='riga',
            options={'verbose_name_plural': 'Righe di menù'},
        ),
        migrations.AddField(
            model_name='um',
            name='tipo',
            field=models.CharField(max_length=20, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='um',
            name='nome',
            field=models.CharField(max_length=20),
        ),
        migrations.AddField(
            model_name='dettaglio',
            name='lista',
            field=models.ForeignKey(to='slista.Lista'),
        ),
    ]
