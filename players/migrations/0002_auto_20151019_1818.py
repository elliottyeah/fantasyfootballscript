# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='player',
            name='expected_next_three',
        ),
        migrations.RemoveField(
            model_name='player',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='player',
            name='points_last_three',
        ),
        migrations.AddField(
            model_name='player',
            name='chance_playing',
            field=models.CharField(default=datetime.datetime(2015, 10, 19, 18, 18, 45, 48344, tzinfo=utc), max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='player',
            name='buy_value',
            field=models.DecimalField(max_digits=4, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='player',
            name='idn',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='player',
            name='last_three',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='player',
            name='news',
            field=models.CharField(max_length=100),
        ),
    ]
