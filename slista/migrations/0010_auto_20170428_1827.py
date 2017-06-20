# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slista', '0009_auto_20170428_1706'),
    ]

    operations = [
        migrations.CreateModel(
            name='Riga',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('quantità', models.DecimalField(max_digits=6, decimal_places=2)),
            ],
            options={
                'verbose_name_plural': 'Righe_menù',
            },
        ),
        migrations.AlterModelOptions(
            name='composizione',
            options={'verbose_name_plural': 'Composizioni'},
        ),
        migrations.AlterModelOptions(
            name='trasformatore',
            options={'verbose_name_plural': 'Conversioni'},
        ),
        migrations.RemoveField(
            model_name='menu',
            name='voce',
        ),
        migrations.RemoveField(
            model_name='utente',
            name='usa',
        ),
        migrations.AddField(
            model_name='voce',
            name='scheda',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='data',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='giorno',
            field=models.SmallIntegerField(blank=True, null=True, choices=[(1, 'lunedì'), (2, 'martedì'), (3, 'mercoledì'), (4, 'giovedì'), (5, 'venerdì'), (6, 'sabato'), (7, 'domenica')]),
        ),
        migrations.AlterField(
            model_name='menu',
            name='nome',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='vocep',
            name='proprietario',
            field=models.ForeignKey(to='slista.Utente', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='riga',
            name='menu',
            field=models.ForeignKey(to='slista.Menu'),
        ),
        migrations.AddField(
            model_name='riga',
            name='voce',
            field=models.ForeignKey(to='slista.Voce'),
        ),
        migrations.AddField(
            model_name='menu',
            name='righe',
            field=models.ManyToManyField(to='slista.Voce', through='slista.Riga', related_name='voci_di'),
        ),
    ]
