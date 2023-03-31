# Generated by Django 4.1.7 on 2023-03-26 18:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeTrack', '0012_alter_times_end_time_alter_times_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='times',
            name='break_length',
            field=models.DurationField(blank=True, default=datetime.timedelta(0), null=True, verbose_name='Time taken for break'),
        ),
    ]