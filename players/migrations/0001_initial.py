# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('team_name', models.CharField(max_length=40)),
                ('player_position', models.CharField(max_length=40)),
                ('buy_value', models.DecimalField(max_digits=2, decimal_places=1)),
                ('next_three', models.CharField(max_length=40)),
                ('last_three', models.CharField(max_length=40)),
                ('points_last_three', models.CharField(max_length=40)),
                ('expected_next_three', models.CharField(max_length=40)),
                ('idn', models.CharField(max_length=40)),
                ('news', models.CharField(max_length=40)),
            ],
        ),
    ]
