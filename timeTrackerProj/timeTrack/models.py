from django.db import models

from django.utils import timezone
import datetime

# Create your models here.


class Times(models.Model):

    date_of_work = models.DateField(
        verbose_name='Day of work', default=timezone.now, blank=True)
    start_time = models.TimeField(
        verbose_name='Start Time', null=True,  blank=True)
    end_time = models.TimeField(
        verbose_name='End Time', null=True, blank=True)
    break_length = models.DurationField(
        verbose_name='Time taken for break', default=datetime.timedelta(0), null=True, blank=True,)

    @property
    def time_worked(self):
        """
        Fn to calculate total time worked from `end_time - start_time - break_length`.
        """

        # check if start and end and break exist before doing calculations
        if (self.start_time != None) and (self.end_time != None) and (self.break_length != None):
            
            #convert Time objects to datetime
            self.start_time_datetime = datetime.datetime.strptime(f"{self.date_of_work} {str(self.start_time)}", '%Y-%m-%d %H:%M:%S')
            self.end_time_datetime = datetime.datetime.strptime(f"{self.date_of_work} {str(self.end_time)}", '%Y-%m-%d %H:%M:%S')
            
            total_secs_worked = (
                self.end_time_datetime - self.start_time_datetime - self.break_length).total_seconds()
            hrs_worked = int(total_secs_worked//3600)
            mins_worked = int((total_secs_worked % 3600)//60)
            return f"{hrs_worked}:{mins_worked}"
        else:
            return 'Incomplete'
    
    def time_worked_str(self):
        """
        Fn to get time worked as string
        """
        if self.time_worked != 'Incomplete':
            # print(f"TIMEWORKED AS STRING: {str(self.time_worked)}")
            time_str = str(self.time_worked).split(':')
            time_str_hr = time_str[0]
            time_str_min = time_str[1]
            return f"{time_str_hr}hrs {time_str_min}mins"
        else:
            return f"Incomplete"

    def __str__(self):
        return f"{self.date_of_work} (hrs worked: {self.time_worked})"