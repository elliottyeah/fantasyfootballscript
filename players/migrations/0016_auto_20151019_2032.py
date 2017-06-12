# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0015_player_expected_points'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='chance_playing',
        ),
        migrations.RemoveField(
            model_name='player',
            name='expected_points',
        ),
        migrations.AddField(
            model_name='player',
            name='expected',
            field=models.CharField(default=b'0', max_length=40),
        ),
        migrations.AlterField(
            model_name='player',
            name='buy_value',
            field=models.DecimalField(max_digits=2, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='player',
            name='idn',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='player',
            name='last_three',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='player',
            name='news',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='player',
            name='next_three',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='player',
            name='player_position',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='player',
            name='team_name',
            field=models.CharField(max_length=40),
        ),
    ]
