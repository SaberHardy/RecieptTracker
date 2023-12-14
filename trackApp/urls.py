from django.urls import path
from trackApp import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.ListItems.as_view(), name='index'),

    # path('login/', views.login, name='login'),
    # path('register/', views.register, name='register'),

    # path('details/<int:id>/', views.details, name='details'),
    path('details/<int:pk>/', login_required(views.ReceiptDetail.as_view()), name='details'),

    path('track_item/', views.track_item, name='track_item'),

    # path('delete_item/<int:id>/', views.delete_item, name='delete_item'),
    path('delete_item/<int:pk>/', login_required(views.DeleteReceiptView.as_view()), name='delete_item'),

    # path('create_receipt/', views.create_receipt, name='create_receipt'),
    path('create_receipt/', login_required(views.CreateReceiptView.as_view()), name='create_receipt'),

    # path('update_receipt/<int:id>/', views.update_receipt, name='update_receipt'),
    path('update_receipt/<int:pk>/', login_required(views.UpdateReceiptView.as_view()), name='update_receipt'),
]
