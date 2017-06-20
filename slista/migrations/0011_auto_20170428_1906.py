# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slista', '0010_auto_20170428_1827'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='composizione',
            options={'verbose_name_plural': 'Composizioni voci'},
        ),
        migrations.AlterModelOptions(
            name='um',
            options={'verbose_name_plural': 'Unità di misura'},
        ),
        migrations.AlterModelOptions(
            name='vocep',
            options={'verbose_name_plural': 'Voci private'},
        ),
        migrations.AddField(
            model_name='trasformatore',
            name='coefficente',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
