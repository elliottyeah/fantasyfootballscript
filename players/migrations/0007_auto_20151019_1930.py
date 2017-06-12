# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0006_auto_20151019_1847'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='buy_value',
        ),
        migrations.AddField(
            model_name='player',
            name='last_name',
            field=models.CharField(default=b'a', max_length=40),
        ),
    ]
