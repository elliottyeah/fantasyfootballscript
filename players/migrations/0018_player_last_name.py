# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0017_player_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='last_name',
            field=models.CharField(default=b'elli', max_length=40),
        ),
    ]
