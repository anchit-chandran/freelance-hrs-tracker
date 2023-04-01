from django import forms
from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']