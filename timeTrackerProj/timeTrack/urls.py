from django.urls import path

from . import views

urlpatterns = [
    path('', views.TimeListView.as_view(), name='index'),
    path('add-time', views.AddTimeView.as_view(), name='addTime')
]