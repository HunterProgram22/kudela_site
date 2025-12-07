from django.urls import path
from . import views

app_name = 'finance'

urlpatterns = [
    path('', views.home, name='home'),
    path('balance/', views.balance_list, name='balance_list'),
]
