from django.db import models

from datetime import date

# Create your models here.
class Times(models.Model):
    
    date_of_work = models.DateField(verbose_name='Day of work', default=date.today())
    start_time = models.TimeField(verbose_name='Start Time')
    end_time = models.TimeField(verbose_name='End Time')
    break_length = models.DurationField(verbose_name='Time taken for break')
    
