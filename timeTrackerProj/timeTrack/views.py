from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from timeTrack.models import Times

from timeTrack.forms import TimeCreateForm


class TimeListView(ListView):

    model = Times
    template_name = 'timeTrack/main.html'
    context_object_name = 'logs'


class AddTimeView(CreateView):
    
    model = Times
    template_name = 'timeTrack/time-add.html'
    form_class = TimeCreateForm
    success_url = reverse_lazy('index')

class UpdateTimeView(UpdateView):
    
    model = Times
    template_name = 'timeTrack/time-update.html'
    form_class = TimeCreateForm
    success_url = reverse_lazy('index')
    
class DeleteTimeView(DeleteView):
    
    model = Times
    success_url = reverse_lazy('index')
