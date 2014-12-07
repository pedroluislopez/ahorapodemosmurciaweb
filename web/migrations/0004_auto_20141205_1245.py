# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_noticia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='titular',
            field=models.CharField(max_length=255, verbose_name=b'Titular'),
            preserve_default=True,
        ),
    ]
