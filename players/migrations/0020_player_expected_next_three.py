# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0019_player_points_last_three'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='expected_next_three',
            field=models.CharField(default=b'elli', max_length=40),
        ),
    ]
