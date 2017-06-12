# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criteria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cash',
            name='cash_option',
            field=models.DecimalField(max_digits=5, decimal_places=1),
        ),
    ]
