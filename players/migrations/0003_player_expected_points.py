# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_auto_20151019_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='expected_points',
            field=models.DecimalField(default=1, max_digits=10, decimal_places=10),
            preserve_default=False,
        ),
    ]
