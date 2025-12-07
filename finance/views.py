from django.shortcuts import render
from .models import MonthBal, MonthInc


def home(request):
    # Get the most recent balance record
    latest_balance = MonthBal.objects.first()  # Already ordered by -date in model

    # Get the most recent income record
    latest_income = MonthInc.objects.first()

    # Get last 12 months of balances for the chart
    recent_balances = MonthBal.objects.all()[:12]

    # Prepare chart data (reversed so oldest is first)
    chart_labels = []
    chart_networth = []
    chart_assets = []
    chart_liabilities = []

    for balance in reversed(list(recent_balances)):
        chart_labels.append(balance.date.strftime('%b %Y'))
        chart_networth.append(float(balance.networth()))
        chart_assets.append(float(balance.total_assets()))
        chart_liabilities.append(float(balance.total_liabilities()))

    context = {
        'latest_balance': latest_balance,
        'latest_income': latest_income,
        'chart_labels': chart_labels,
        'chart_networth': chart_networth,
        'chart_assets': chart_assets,
        'chart_liabilities': chart_liabilities,
    }

    return render(request, 'finance/home.html', context)


def balance_list(request):
    # Get all balance records
    balances = MonthBal.objects.all()

    # Get filter parameters
    year = request.GET.get('year')
    if year:
        balances = balances.filter(date__year=year)

    # Get available years for filter dropdown
    available_years = MonthBal.objects.dates('date', 'year', order='DESC')

    context = {
        'balances': balances,
        'available_years': available_years,
        'selected_year': year,
    }

    return render(request, 'finance/balance_list.html', context)


def income_list(request):
    # Get all income records
    incomes = MonthInc.objects.all()

    # Get filter parameters
    year = request.GET.get('year')
    if year:
        incomes = incomes.filter(date__year=year)

    # Get available years for filter dropdown
    available_years = MonthInc.objects.dates('date', 'year', order='DESC')

    context = {
        'incomes': incomes,
        'available_years': available_years,
        'selected_year': year,
    }

    return render(request, 'finance/income_list.html', context)
