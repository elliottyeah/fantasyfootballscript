# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0020_player_expected_next_three'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='expected_next_three',
        ),
        migrations.RemoveField(
            model_name='player',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='player',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='player',
            name='points_last_three',
        ),
    ]
