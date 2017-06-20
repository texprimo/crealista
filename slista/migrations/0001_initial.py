# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Composizione',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('quantitaP', models.DecimalField(max_digits=6, decimal_places=2)),
                ('quantitaI', models.DecimalField(max_digits=6, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('data', models.DateField()),
                ('giorno', models.SmallIntegerField()),
                ('nome', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Trasformatore',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='UM',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('nome', models.CharField(max_length=8)),
                ('corrisponde', models.ManyToManyField(through='slista.Trasformatore', to='slista.UM', related_name='da')),
            ],
        ),
        migrations.CreateModel(
            name='Utente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('livello', models.CharField(max_length=1)),
                ('note', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Voce',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('nome', models.CharField(max_length=40)),
                ('descrizione', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='VoceP',
            fields=[
                ('voce_ptr', models.OneToOneField(serialize=False, parent_link=True, auto_created=True, primary_key=True, to='slista.Voce')),
            ],
            bases=('slista.voce',),
        ),
        migrations.AddField(
            model_name='voce',
            name='UM',
            field=models.ForeignKey(to='slista.UM'),
        ),
        migrations.AddField(
            model_name='voce',
            name='ingredienti',
            field=models.ManyToManyField(through='slista.Composizione', to='slista.Voce', related_name='ingrediente_di'),
        ),
        migrations.AddField(
            model_name='utente',
            name='usa',
            field=models.ManyToManyField(through='slista.Menu', to='slista.Voce', related_name='utilizzato_da'),
        ),
        migrations.AddField(
            model_name='trasformatore',
            name='UMEntrata',
            field=models.ForeignKey(related_name='convertibile', to='slista.UM'),
        ),
        migrations.AddField(
            model_name='trasformatore',
            name='UMUscita',
            field=models.ForeignKey(related_name='converte_da', to='slista.UM'),
        ),
        migrations.AddField(
            model_name='menu',
            name='utentek',
            field=models.ForeignKey(to='slista.Utente'),
        ),
        migrations.AddField(
            model_name='menu',
            name='voce',
            field=models.ForeignKey(to='slista.Voce'),
        ),
        migrations.AddField(
            model_name='composizione',
            name='ingrediente',
            field=models.ForeignKey(related_name='parte_di', to='slista.Voce'),
        ),
        migrations.AddField(
            model_name='composizione',
            name='prodotto',
            field=models.ForeignKey(related_name='elementi', to='slista.Voce'),
        ),
        migrations.AddField(
            model_name='vocep',
            name='proprietario',
            field=models.ForeignKey(to='slista.Utente'),
        ),
    ]
