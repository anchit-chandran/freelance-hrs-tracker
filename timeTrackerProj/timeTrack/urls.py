from django.urls import path

from . import views

urlpatterns = [
    path('', views.TimeListView.as_view(), name='index'),
    path('add-time', views.AddTimeView.as_view(), name='addTime'),
    path('sign-up', views.sign_up, name='sign-up'),
    path('logout', views.signout, name='logout'),
    path('update-time/<int:pk>', views.UpdateTimeView.as_view(), name='updateTime'),
    path('delete-time/<int:pk>', views.DeleteTimeView.as_view(), name='deleteTime'),
    path('view-calculations', views.viewCalculations, name='viewCalculations')
]