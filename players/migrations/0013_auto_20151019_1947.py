# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0012_auto_20151019_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='buy_value',
            field=models.DecimalField(default=9.1, max_digits=2, decimal_places=1),
        ),
        migrations.AddField(
            model_name='player',
            name='chance_playing',
            field=models.CharField(default=b'100', max_length=10),
        ),
        migrations.AddField(
            model_name='player',
            name='idn',
            field=models.CharField(default=999, max_length=3),
        ),
        migrations.AddField(
            model_name='player',
            name='last_three',
            field=models.CharField(default=b'100', max_length=80),
        ),
        migrations.AddField(
            model_name='player',
            name='news',
            field=models.CharField(default=b'100', max_length=100),
        ),
        migrations.AddField(
            model_name='player',
            name='next_three',
            field=models.CharField(default=b'100', max_length=40),
        ),
        migrations.AddField(
            model_name='player',
            name='player_position',
            field=models.CharField(default=b'100', max_length=40),
        ),
        migrations.AddField(
            model_name='player',
            name='team_name',
            field=models.CharField(default=b'100', max_length=40),
        ),
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(default=b'100', max_length=40),
        ),
    ]
