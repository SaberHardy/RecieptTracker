from django.urls import path
from trackApp import views

urlpatterns = [
    path('', views.index, name='index'),
]
