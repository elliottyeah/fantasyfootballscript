# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0009_player_expected_points'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='expected_points',
        ),
    ]
