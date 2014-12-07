# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=255, verbose_name=b'T\xc3\xadtulo')),
                ('slug', models.SlugField(max_length=60, verbose_name=b'Texto enlace')),
                ('entradilla', models.TextField(max_length=512, verbose_name=b'Entradilla')),
                ('cuerpo', ckeditor.fields.RichTextField(verbose_name=b'Cuerpo')),
                ('publicado', models.DateField(verbose_name=b'Publicado')),
            ],
            options={
                'verbose_name': 'Publicaci\xf3n',
                'verbose_name_plural': 'Publicaciones',
            },
            bases=(models.Model,),
        ),
    ]
