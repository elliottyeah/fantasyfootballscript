# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0014_auto_20151019_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='expected_points',
            field=models.DecimalField(default=1.1, max_digits=25, decimal_places=20),
        ),
    ]
