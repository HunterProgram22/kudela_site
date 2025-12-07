from django.urls import path
from . import views

app_name = 'finance'

urlpatterns = [
    path('', views.home, name='home'),
    path('balance/', views.balance_list, name='balance_list'),
    path('balance/add/', views.balance_add, name='balance_add'),
    path('balance/<int:pk>/edit/', views.balance_edit, name='balance_edit'),
    path('income/', views.income_list, name='income_list'),
    path('income/add/', views.income_add, name='income_add'),
    path('income/<int:pk>/edit/', views.income_edit, name='income_edit'),
    path('taxes/', views.tax_list, name='tax_list'),
    path('taxes/add/', views.tax_add, name='tax_add'),
    path('taxes/<int:pk>/edit/', views.tax_edit, name='tax_edit'),
    path('analysis/', views.analysis, name='analysis'),
    path('reports/', views.reports, name='reports'),
]
