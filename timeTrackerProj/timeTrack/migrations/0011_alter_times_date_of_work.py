# Generated by Django 4.1.7 on 2023-03-25 08:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('timeTrack', '0010_alter_times_date_of_work'),
    ]

    operations = [
        migrations.AlterField(
            model_name='times',
            name='date_of_work',
            field=models.DateField(blank=True, default=django.utils.timezone.now, verbose_name='Day of work'),
        ),
    ]
