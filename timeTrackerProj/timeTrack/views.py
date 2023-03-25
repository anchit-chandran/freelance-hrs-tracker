from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic.list import ListView

from timeTrack.models import Times

class ArticleDetailView(ListView):

    model = Times
    template_name = 'timeTrack/home.html'
    context_object_name = 'logs'
