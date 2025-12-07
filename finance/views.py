from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import MonthBal, MonthInc, TaxReturn
from .forms import MonthBalForm, MonthIncForm, TaxReturnForm

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


def balance_add(request):
    if request.method == 'POST':
        form = MonthBalForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Balance record added successfully!')
            return redirect('finance:balance_list')
    else:
        form = MonthBalForm()

    # Group fields for organized display
    field_groups = {
        'Checking Accounts': ['huntington_check', 'fifththird_check'],
        'Savings Accounts': ['huntington_save', 'fifththird_save', 'capone_save', 'amex_save'],
        'Investments': ['robinhood_invest', 'deacon_invest', 'buckeye_invest'],
        'Retirement': ['opers_retire', 'four57_retire', 'four01_retire', 'roth_retire'],
        'Property': ['main_home', 'justin_car', 'kat_car'],
        'Credit Cards': ['capone_credit', 'amex_credit', 'discover_credit'],
        'Loans': ['car_loan', 'pubstudent_loan', 'privstudent_loan', 'main_mortgage'],
    }

    context = {
        'form': form,
        'field_groups': field_groups,
    }

    return render(request, 'finance/balance_form.html', context)


def income_add(request):
    if request.method == 'POST':
        form = MonthIncForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Income record added successfully!')
            return redirect('finance:income_list')
    else:
        form = MonthIncForm()

    # Group fields for organized display
    field_groups = {
        'Interest Income': ['huntington_interest', 'fifththird_interest', 'capone_interest', 'amex_interest', 'schwab_interest'],
        'Salary & Dividends': ['supremecourt_salary', 'cdm_salary', 'schwab_dividends'],
        'Other Income': ['expense_checks', 'miscellaneous_income', 'refund_rebate_repayment', 'gift_income'],
        'Retirement Contributions': ['opers_retirement', 'four57b_retirement', 'four01k_retirement', 'roth_retirement'],
        'Investment Contributions': ['robinhood_investments', 'schwab_investments'],
        'Savings Contributions': ['amex_savings', 'fifththird_savings', 'capone_savings', 'five29_college', 'huntington_savings'],
        'Taxes': ['federal_tax', 'social_security', 'medicare', 'ohio_tax', 'columbus_tax'],
        'Benefits': ['health_insurance', 'supplementallife_insurance', 'flex_spending', 'cdm_std', 'cdmsupplemental_ltd', 'parking', 'parking_admin'],
        'Housing': ['main_mortgage', 'hoa_fees'],
        'Utilities': ['aep_electric', 'rumpke_trash', 'delaware_sewer', 'delco_water', 'suburban_gas', 'verizon_kat', 'sprint_justin', 'directtv_cable', 'timewarner_internet'],
        'Loans': ['caponeauto_loan', 'public_loan', 'private_loan'],
        'Credit Cards': ['capone_creditcard', 'amex_creditcard', 'discover_creditcard', 'kohls_vicsec_macy_eddiebauer_creditcards', 'katwork_creditcard'],
        'Other Expenses': ['auto_insurance', 'cashorcheck_purchases', 'daycare', 'taxdeductible_giving'],
    }

    context = {
        'form': form,
        'field_groups': field_groups,
    }

    return render(request, 'finance/income_form.html', context)


def balance_edit(request, pk):
    balance = get_object_or_404(MonthBal, pk=pk)

    if request.method == 'POST':
        form = MonthBalForm(request.POST, instance=balance)
        if form.is_valid():
            form.save()
            messages.success(request, 'Balance record updated successfully!')
            return redirect('finance:balance_list')
    else:
        form = MonthBalForm(instance=balance)

    field_groups = {
        'Checking Accounts': ['huntington_check', 'fifththird_check'],
        'Savings Accounts': ['huntington_save', 'fifththird_save', 'capone_save', 'amex_save'],
        'Investments': ['robinhood_invest', 'deacon_invest', 'buckeye_invest'],
        'Retirement': ['opers_retire', 'four57_retire', 'four01_retire', 'roth_retire'],
        'Property': ['main_home', 'justin_car', 'kat_car'],
        'Credit Cards': ['capone_credit', 'amex_credit', 'discover_credit'],
        'Loans': ['car_loan', 'pubstudent_loan', 'privstudent_loan', 'main_mortgage'],
    }

    context = {
        'form': form,
        'field_groups': field_groups,
        'editing': True,
        'balance': balance,
    }

    return render(request, 'finance/balance_form.html', context)


def income_edit(request, pk):
    income = get_object_or_404(MonthInc, pk=pk)

    if request.method == 'POST':
        form = MonthIncForm(request.POST, instance=income)
        if form.is_valid():
            form.save()
            messages.success(request, 'Income record updated successfully!')
            return redirect('finance:income_list')
    else:
        form = MonthIncForm(instance=income)

    field_groups = {
        'Interest Income': ['huntington_interest', 'fifththird_interest', 'capone_interest',
                            'amex_interest', 'schwab_interest'],
        'Salary & Dividends': ['supremecourt_salary', 'cdm_salary', 'schwab_dividends'],
        'Other Income': ['expense_checks', 'miscellaneous_income', 'refund_rebate_repayment',
                         'gift_income'],
        'Retirement Contributions': ['opers_retirement', 'four57b_retirement', 'four01k_retirement',
                                     'roth_retirement'],
        'Investment Contributions': ['robinhood_investments', 'schwab_investments'],
        'Savings Contributions': ['amex_savings', 'fifththird_savings', 'capone_savings',
                                  'five29_college', 'huntington_savings'],
        'Taxes': ['federal_tax', 'social_security', 'medicare', 'ohio_tax', 'columbus_tax'],
        'Benefits': ['health_insurance', 'supplementallife_insurance', 'flex_spending', 'cdm_std',
                     'cdmsupplemental_ltd', 'parking', 'parking_admin'],
        'Housing': ['main_mortgage', 'hoa_fees'],
        'Utilities': ['aep_electric', 'rumpke_trash', 'delaware_sewer', 'delco_water',
                      'suburban_gas', 'verizon_kat', 'sprint_justin', 'directtv_cable',
                      'timewarner_internet'],
        'Loans': ['caponeauto_loan', 'public_loan', 'private_loan'],
        'Credit Cards': ['capone_creditcard', 'amex_creditcard', 'discover_creditcard',
                         'kohls_vicsec_macy_eddiebauer_creditcards', 'katwork_creditcard'],
        'Other Expenses': ['auto_insurance', 'cashorcheck_purchases', 'daycare',
                           'taxdeductible_giving'],
    }

    context = {
        'form': form,
        'field_groups': field_groups,
        'editing': True,
        'income': income,
    }

    return render(request, 'finance/income_form.html', context)


def tax_list(request):
    taxes = TaxReturn.objects.all()

    context = {
        'taxes': taxes,
    }

    return render(request, 'finance/tax_list.html', context)


def tax_add(request):
    if request.method == 'POST':
        form = TaxReturnForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tax return added successfully!')
            return redirect('finance:tax_list')
    else:
        form = TaxReturnForm()

    context = {
        'form': form,
    }

    return render(request, 'finance/tax_form.html', context)


def tax_edit(request, pk):
    tax = get_object_or_404(TaxReturn, pk=pk)

    if request.method == 'POST':
        form = TaxReturnForm(request.POST, instance=tax)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tax return updated successfully!')
            return redirect('finance:tax_list')
    else:
        form = TaxReturnForm(instance=tax)

    context = {
        'form': form,
        'editing': True,
        'tax': tax,
    }

    return render(request, 'finance/tax_form.html', context)

