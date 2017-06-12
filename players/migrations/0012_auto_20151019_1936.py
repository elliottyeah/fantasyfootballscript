# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0011_player_expected_points'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='buy_value',
        ),
        migrations.RemoveField(
            model_name='player',
            name='chance_playing',
        ),
        migrations.RemoveField(
            model_name='player',
            name='expected_points',
        ),
        migrations.RemoveField(
            model_name='player',
            name='idn',
        ),
        migrations.RemoveField(
            model_name='player',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='player',
            name='last_three',
        ),
        migrations.RemoveField(
            model_name='player',
            name='news',
        ),
        migrations.RemoveField(
            model_name='player',
            name='next_three',
        ),
        migrations.RemoveField(
            model_name='player',
            name='player_position',
        ),
        migrations.RemoveField(
            model_name='player',
            name='team_name',
        ),
    ]
