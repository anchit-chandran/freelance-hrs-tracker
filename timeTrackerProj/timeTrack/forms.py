from django import forms

from .views import Times

class TimeCreateForm(forms.ModelForm):
    class Meta:
        model = Times
        fields = '__all__'