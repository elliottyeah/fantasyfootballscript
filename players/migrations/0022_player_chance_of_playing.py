# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0021_auto_20151019_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='chance_of_playing',
            field=models.CharField(default='100', max_length=40),
            preserve_default=False,
        ),
    ]
