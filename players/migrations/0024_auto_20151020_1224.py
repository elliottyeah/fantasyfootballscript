# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0023_auto_20151020_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='buy_value',
            field=models.DecimalField(max_digits=4, decimal_places=2),
        ),
    ]
