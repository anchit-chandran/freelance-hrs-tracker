from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

from django.db.models import Sum, DurationField, ExpressionWrapper, F

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from timeTrack.models import Times

from timeTrack.forms import TimeCreateForm, RegisterForm

from timeTrack.calculate_tax import calculate_takehome


class TimeListView(LoginRequiredMixin, ListView):

    login_url = '/login/'
    redirect_field_name = 'redirect_to'

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

            context['takehome'] = calculate_takehome(total_hrs=158)

        return context


def viewCalculations(request):
    
    default_calc_str = 'No calculations!'
    total_hrs = default_calc_str
    takehome = default_calc_str

    # check if ang logs exist
    if Times.objects.all().exists():
        # Calculate total hrs as float
        total_hrs_dict = Times.objects.annotate(shift_length=ExpressionWrapper(
            F('end_time') - F('start_time'),
            output_field=DurationField()
        )).aggregate(total_hrs=Sum('shift_length'))

        # convert into total hours
        total_hrs = total_hrs_dict['total_hrs'].total_seconds() / 3600
        
        takehome = calculate_takehome(total_hrs=158)
        
    return render(request, template_name='timeTrack/calculations.html', context={'total_hr' : total_hrs, 'takehome':takehome})


class AddTimeView(LoginRequiredMixin, CreateView):

    model = Times
    template_name = 'timeTrack/time-add.html'
    form_class = TimeCreateForm
    success_url = reverse_lazy('index')


class UpdateTimeView(LoginRequiredMixin, UpdateView):

    model = Times
    template_name = 'timeTrack/time-update.html'
    form_class = TimeCreateForm
    success_url = reverse_lazy('index')


class DeleteTimeView(LoginRequiredMixin, DeleteView):

    model = Times
    success_url = reverse_lazy('index')


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('index'))
    else:
        form = RegisterForm()
    return render(request, 'registration/sign-up.html', context={'form': form})


def signout(request):
    logout(request)
    return redirect(reverse('login'))
