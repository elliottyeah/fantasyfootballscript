# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0003_player_expected_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='expected_points',
            field=models.DecimalField(max_digits=6, decimal_places=4),
        ),
    ]
