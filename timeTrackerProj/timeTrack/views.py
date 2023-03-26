from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from timeTrack.models import Times

from timeTrack.forms import TimeCreateForm


class TimeListView(ListView):

    model = Times
    template_name = 'timeTrack/home.html'
    context_object_name = 'logs'


class AddTimeView(CreateView):
    
    model = Times
    template_name = 'timeTrack/time-add.html'
    form_class = TimeCreateForm
    success_url = reverse_lazy('index')
