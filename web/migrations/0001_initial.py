# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50, verbose_name=b'Nombre')),
                ('apellidos', models.CharField(max_length=50, verbose_name=b'Apellidos')),
                ('imagen', models.ImageField(upload_to=b'profile_images', verbose_name=b'Imagen', blank=True)),
                ('secretario', models.BooleanField(default=False, verbose_name=b'Secretario General')),
                ('consejo', models.BooleanField(default=False, verbose_name=b'Consejo Ciudadano')),
                ('motivacion', models.TextField(max_length=1000, verbose_name=b'Motivaci\xc3\xb3n', blank=True)),
                ('orden', models.IntegerField(verbose_name=b'Orden')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
