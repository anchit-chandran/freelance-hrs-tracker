from django import forms
from django.forms import ModelForm

from .views import Times

class DateInput(forms.DateInput):
    input_type = 'date'
class TimeInput(forms.TimeInput):
    input_type = 'time'
    
class TimeCreateForm(ModelForm):
             
    class Meta:
        model = Times
        fields = '__all__'
        widgets = {
            'date_of_work': DateInput(),
            'start_time' : TimeInput(),
            'end_time' : TimeInput(),
            'break_length' : TimeInput(),
        }