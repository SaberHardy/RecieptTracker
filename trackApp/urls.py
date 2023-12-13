from django.urls import path
from trackApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('details/<int:id>/', views.details, name='details'),
    path('track_item/', views.track_item, name='track_item'),
    path('delete_item/<int:id>/', views.delete_item, name='delete_item'),
]
