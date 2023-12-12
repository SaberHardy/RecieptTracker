from django.urls import path
from trackApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('details/<int:id>/', views.details, name='details'),
]
