# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slista', '0012_utente_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='utente',
            name='usid',
        ),
    ]
