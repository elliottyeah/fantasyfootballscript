# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0004_auto_20151019_1845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='expected_points',
        ),
    ]
