# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0007_auto_20151019_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='buy_value',
            field=models.DecimalField(default=9.1, max_digits=2, decimal_places=1),
        ),
    ]
