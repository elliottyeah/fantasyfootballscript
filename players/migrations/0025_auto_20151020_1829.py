# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0024_auto_20151020_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='expected',
            field=models.DecimalField(default=0.0, max_digits=20, decimal_places=10),
        ),
    ]
