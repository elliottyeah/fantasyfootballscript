# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0010_remove_player_expected_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='expected_points',
            field=models.CharField(default='a', max_length=100),
            preserve_default=False,
        ),
    ]
