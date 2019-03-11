# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TServer',
            fields=[
                ('app', models.CharField(max_length=64, serialize=False, primary_key=True)),
                ('server', models.CharField(max_length=64)),
                ('division', models.CharField(max_length=64)),
                ('node', models.CharField(max_length=64)),
                ('status', models.IntegerField()),
                ('use_agent', models.IntegerField()),
            ],
            options={
                'db_table': 't_server',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TService',
            fields=[
                ('app', models.CharField(max_length=64, serialize=False, primary_key=True)),
                ('server', models.CharField(max_length=64)),
                ('division', models.CharField(max_length=64)),
                ('node', models.CharField(max_length=64)),
                ('service', models.CharField(max_length=128)),
                ('endpoint', models.CharField(max_length=512)),
            ],
            options={
                'db_table': 't_service',
                'managed': True,
            },
        ),
        migrations.AlterUniqueTogether(
            name='tservice',
            unique_together=set([('app', 'server', 'division', 'node', 'service')]),
        ),
        migrations.AlterUniqueTogether(
            name='tserver',
            unique_together=set([('app', 'server', 'division', 'node')]),
        ),
    ]
