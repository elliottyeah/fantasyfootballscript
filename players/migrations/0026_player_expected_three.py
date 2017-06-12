# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0025_auto_20151020_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='expected_three',
            field=models.IntegerField(default=0),
        ),
    ]
