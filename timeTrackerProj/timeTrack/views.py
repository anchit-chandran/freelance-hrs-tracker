from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy

from django.db.models import Sum, DurationField, ExpressionWrapper, F

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from timeTrack.models import Times

from timeTrack.forms import TimeCreateForm


class TimeListView(ListView):

    model = Times
    template_name = 'timeTrack/main.html'
    context_object_name = 'logs'
    ordering = ['-date_of_work']

    # extra context
    def get_context_data(self, **kwargs):

        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        # check if ang logs exist
        if Times.objects.all().exists():
            # Calculate total hrs as float
            total_hrs_dict = Times.objects.annotate(shift_length=ExpressionWrapper(
                F('end_time') - F('start_time'),
                output_field=DurationField()
            )).aggregate(total_hrs=Sum('shift_length'))

            # convert into total hours
            total_hrs = total_hrs_dict['total_hrs'].total_seconds() / 3600
            context['total_hrs'] = total_hrs
            
            #convert into total earned
            rate_ph = 25
            context['total_earned'] = round(total_hrs * rate_ph, 2)
        
        return context


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
