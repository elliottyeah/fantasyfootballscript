# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0005_remove_player_expected_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='buy_value',
            field=models.DecimalField(max_digits=4, decimal_places=2),
        ),
    ]
