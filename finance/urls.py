from django.urls import path
from . import views

app_name = 'finance'

urlpatterns = [
    path('', views.home, name='home'),
    path('balance/', views.balance_list, name='balance_list'),
    path('balance/add/', views.balance_add, name='balance_add'),
    path('income/', views.income_list, name='income_list'),
    path('income/add/', views.income_add, name='income_add'),
]
