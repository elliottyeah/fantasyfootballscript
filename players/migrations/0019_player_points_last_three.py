# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0018_player_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='points_last_three',
            field=models.CharField(default=b'elli', max_length=40),
        ),
    ]
