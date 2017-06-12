# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0008_player_buy_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='expected_points',
            field=models.DecimalField(default=9.1, max_digits=6, decimal_places=4),
        ),
    ]
