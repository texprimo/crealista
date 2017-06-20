# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slista', '0018_auto_20170618_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voce',
            name='tipo',
            field=models.CharField(max_length=40, choices=[('P', 'Prodotto'), ('S', 'Semilavorato'), ('I', 'Ingrediente')], blank=True, null=True),
        ),
    ]
