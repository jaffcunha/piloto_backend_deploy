# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome_pessoa', models.CharField(max_length=64, verbose_name=b'Nome completo')),
                ('idade', models.IntegerField(max_length=16, verbose_name=b'Idade')),
                ('genero', models.CharField(max_length=64, verbose_name=b'Genero')),
                ('cpf', models.CharField(max_length=64, verbose_name=b'CPF')),
                ('empresa', models.CharField(max_length=64, verbose_name=b'Empresa')),
                ('cargo', models.CharField(max_length=64, verbose_name=b'Cargo ocupado')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
