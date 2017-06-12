# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0016_auto_20151019_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='first_name',
            field=models.CharField(default='elliott', max_length=40),
            preserve_default=False,
        ),
    ]
