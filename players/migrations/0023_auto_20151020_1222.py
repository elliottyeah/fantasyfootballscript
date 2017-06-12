# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0022_player_chance_of_playing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='chance_of_playing',
            field=models.CharField(max_length=40, blank=b'true'),
        ),
    ]
