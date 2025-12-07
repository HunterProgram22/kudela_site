from django.contrib import admin
from .models import MonthBal, MonthInc, TaxReturn, MetricConstants


@admin.register(MonthBal)
class MonthBalAdmin(admin.ModelAdmin):
    list_display = ('date', 'networth', 'total_assets', 'total_liabilities')
    list_filter = ('date',)
    ordering = ('-date',)


@admin.register(MonthInc)
class MonthIncAdmin(admin.ModelAdmin):
    list_display = ('date', 'total_income', 'total_expenses', 'total_surplus')
    list_filter = ('date',)
    ordering = ('-date',)


@admin.register(TaxReturn)
class TaxReturnAdmin(admin.ModelAdmin):
    list_display = ('year', 'adjusted_gross_income', 'total_refund')
    ordering = ('-year',)


@admin.register(MetricConstants)
class MetricConstantsAdmin(admin.ModelAdmin):
    list_display = ('date', 'value')
    ordering = ('-date',)
