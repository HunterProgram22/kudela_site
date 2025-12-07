from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from decimal import Decimal
from .models import MonthBal, MonthInc, TaxReturn
from .forms import MonthBalForm, MonthIncForm, TaxReturnForm


@login_required
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


@login_required
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


@login_required
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


@login_required
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


@login_required
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


@login_required
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


@login_required
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


@login_required
def tax_list(request):
    taxes = TaxReturn.objects.all()

    context = {
        'taxes': taxes,
    }

    return render(request, 'finance/tax_list.html', context)


@login_required
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


@login_required
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


@login_required
def analysis(request):
    # Define available categories for analysis
    balance_categories = {
        'Net Worth': 'networth',
        'Total Assets': 'total_assets',
        'Total Liabilities': 'total_liabilities',
        'Checking': 'total_check',
        'Savings': 'total_save',
        'Investments': 'total_invest',
        'Retirement': 'total_retire',
        'Property': 'total_property',
        'Credit Cards': 'total_credit',
        'Loans': 'total_loan',
    }

    income_categories = {
        'Total Income': 'total_income',
        'Total Salary': 'total_salary',
        'Total Expenses': 'total_expenses',
        'Total Surplus': 'total_surplus',
        'Total Taxes': 'total_taxes',
        'Total Savings': 'total_allsavings',
        'Total Utilities': 'total_utilities',
        'Total Housing': 'total_housing',
    }

    # Get filter parameters
    data_type = request.GET.get('type', 'balance')
    category = request.GET.get('category', 'networth')
    year = request.GET.get('year', '')

    # Determine which categories to show
    if data_type == 'income':
        categories = income_categories
        if category not in income_categories.values():
            category = 'total_income'
    else:
        categories = balance_categories
        if category not in balance_categories.values():
            category = 'networth'

    # Get data based on type
    if data_type == 'income':
        queryset = MonthInc.objects.all().order_by('date')
        available_years = MonthInc.objects.dates('date', 'year', order='DESC')
    else:
        queryset = MonthBal.objects.all().order_by('date')
        available_years = MonthBal.objects.dates('date', 'year', order='DESC')

    # Filter by year if specified
    if year:
        queryset = queryset.filter(date__year=year)

    # Build chart data
    chart_labels = []
    chart_data = []

    for record in queryset:
        chart_labels.append(record.date.strftime('%b %Y'))
        # Get the value - either call the method or get the attribute
        value = getattr(record, category)
        if callable(value):
            value = value()
        chart_data.append(float(value))

    # Get current category display name
    all_categories = {**balance_categories, **income_categories}
    category_name = [k for k, v in all_categories.items() if v == category][
        0] if category in all_categories.values() else category

    context = {
        'data_type': data_type,
        'category': category,
        'category_name': category_name,
        'selected_year': year,
        'balance_categories': balance_categories,
        'income_categories': income_categories,
        'available_years': available_years,
        'chart_labels': chart_labels,
        'chart_data': chart_data,
    }

    return render(request, 'finance/analysis.html', context)


@login_required
def get_quarter_data(quarter, year):
    """Get income and balance data for a specific quarter."""
    # Define quarter month ranges
    quarter_months = {
        1: (1, 2, 3),
        2: (4, 5, 6),
        3: (7, 8, 9),
        4: (10, 11, 12),
    }

    months = quarter_months[quarter]

    # Get income records for the quarter
    incomes = MonthInc.objects.filter(
        date__year=year,
        date__month__in=months
    )

    # Aggregate income data
    totals = {
        'income': sum(i.total_income() for i in incomes),
        'expenses': sum(i.total_expenses() for i in incomes),
        'savings': sum(i.total_allsavings() for i in incomes),
        'surplus': sum(i.total_surplus() for i in incomes),
        'taxes': sum(i.total_taxes() for i in incomes),
        'utilities': sum(i.total_utilities() for i in incomes),
        'housing': sum(i.total_housing() for i in incomes),
        'credit_cards': sum(i.total_personal_creditcards() for i in incomes),
    }

    # Get end-of-quarter balance
    # For Q1-Q3, get the first month of next quarter
    # For Q4, get January of next year
    if quarter == 4:
        balance_month = 1
        balance_year = year + 1
    else:
        balance_month = months[-1] + 1
        balance_year = year

    balance = MonthBal.objects.filter(
        date__year=balance_year,
        date__month=balance_month
    ).first()

    if balance:
        totals['networth'] = balance.networth()
        totals['assets'] = balance.total_assets()
        totals['liabilities'] = balance.total_liabilities()
        totals['loan_balance'] = balance.total_loan()
        totals['savings_balance'] = balance.total_save()
    else:
        totals['networth'] = None
        totals['assets'] = None
        totals['liabilities'] = None
        totals['loan_balance'] = None
        totals['savings_balance'] = None

    return totals


@login_required
def reports(request):
    # Get available years from data
    available_years = MonthInc.objects.dates('date', 'year', order='DESC')

    # Get selected quarter and year from request
    selected_quarter = request.GET.get('quarter')

    # Default to most recent complete quarter
    if not selected_quarter and available_years:
        from datetime import date
        today = date.today()
        current_quarter = (today.month - 1) // 3 + 1
        current_year = today.year

        # Go back one quarter for "most recent complete"
        if current_quarter == 1:
            selected_quarter = f"4-{current_year - 1}"
        else:
            selected_quarter = f"{current_quarter - 1}-{current_year}"

    # Parse selection
    quarter_data = None
    last_quarter_data = None
    year_ago_data = None

    if selected_quarter:
        try:
            q, y = selected_quarter.split('-')
            quarter = int(q)
            year = int(y)

            # Current quarter data
            quarter_data = get_quarter_data(quarter, year)
            quarter_data['name'] = f"Q{quarter} {year}"

            # Last quarter data
            if quarter == 1:
                last_q, last_y = 4, year - 1
            else:
                last_q, last_y = quarter - 1, year
            last_quarter_data = get_quarter_data(last_q, last_y)
            last_quarter_data['name'] = f"Q{last_q} {last_y}"

            # Year ago data
            year_ago_data = get_quarter_data(quarter, year - 1)
            year_ago_data['name'] = f"Q{quarter} {year - 1}"

        except (ValueError, TypeError):
            pass

    # Build quarter options for dropdown
    quarter_options = []
    for year_date in available_years:
        for q in [4, 3, 2, 1]:
            quarter_options.append({
                'value': f"{q}-{year_date.year}",
                'label': f"Q{q} {year_date.year}"
            })

    context = {
        'quarter_options': quarter_options,
        'selected_quarter': selected_quarter,
        'quarter_data': quarter_data,
        'last_quarter_data': last_quarter_data,
        'year_ago_data': year_ago_data,
    }

    return render(request, 'finance/reports.html', context)

