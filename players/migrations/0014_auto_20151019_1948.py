# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0013_auto_20151019_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='buy_value',
            field=models.FloatField(default=10),
        ),
    ]
