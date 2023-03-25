from django.urls import path

from . import views

urlpatterns = [
    path('', views.ArticleDetailView.as_view(), name='index'),
]