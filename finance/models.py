from django.db import models
from decimal import Decimal


class MonthBal(models.Model):
    """Monthly balance sheet snapshot - tracks assets and liabilities."""

    date = models.DateField()

    # Checking accounts
    huntington_check = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    fifththird_check = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    # Savings accounts
    huntington_save = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    fifththird_save = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    capone_save = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    amex_save = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    # Investment accounts
    robinhood_invest = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    deacon_invest = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    buckeye_invest = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    # Retirement accounts
    opers_retire = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    four57_retire = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    four01_retire = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    roth_retire = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    # Property
    main_home = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    justin_car = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    kat_car = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    # Credit cards (liabilities)
    capone_credit = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    amex_credit = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    discover_credit = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    # Loans (liabilities)
    car_loan = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    pubstudent_loan = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    privstudent_loan = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    main_mortgage = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    class Meta:
        ordering = ['-date']
        verbose_name = 'Monthly Balance'
        verbose_name_plural = 'Monthly Balances'
        db_table = 'Finance_monthbal'  # Match existing table name

    def __str__(self):
        return f"Balance {self.date.strftime('%B %Y')}"

    # Asset calculations
    def total_check(self):
        return self.huntington_check + self.fifththird_check

    def total_save(self):
        return (self.huntington_save + self.fifththird_save +
                self.capone_save + self.amex_save)

    def total_invest(self):
        return self.robinhood_invest + self.deacon_invest + self.buckeye_invest

    def total_retire(self):
        return (self.opers_retire + self.four57_retire +
                self.four01_retire + self.roth_retire)

    def total_property(self):
        return self.main_home + self.justin_car + self.kat_car

    def total_assets(self):
        return (self.total_check() + self.total_save() +
                self.total_invest() + self.total_retire() +
                self.total_property())

    # Liability calculations
    def total_credit(self):
        return self.capone_credit + self.amex_credit + self.discover_credit

    def total_loan(self):
        return (self.car_loan + self.pubstudent_loan +
                self.privstudent_loan + self.main_mortgage)

    def total_liabilities(self):
        return self.total_credit() + self.total_loan()

    def networth(self):
        return self.total_assets() - self.total_liabilities()


class MonthInc(models.Model):
    """Monthly income and expense tracking."""

    date = models.DateField()

    # Interest income
    huntington_interest = models.DecimalField(max_digits=10, decimal_places=2,
                                              default=Decimal('0.00'))
    fifththird_interest = models.DecimalField(max_digits=10, decimal_places=2,
                                              default=Decimal('0.00'))
    capone_interest = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    amex_interest = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    schwab_interest = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    # Investment income
    schwab_dividends = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    # Other income
    expense_checks = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    miscellaneous_income = models.DecimalField(max_digits=10, decimal_places=2,
                                               default=Decimal('0.00'))
    refund_rebate_repayment = models.DecimalField(max_digits=10, decimal_places=2,
                                                  default=Decimal('0.00'))
    gift_income = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    # Salary income
    supremecourt_salary = models.DecimalField(max_digits=10, decimal_places=2,
                                              default=Decimal('0.00'))
    cdm_salary = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    # Retirement contributions
    opers_retirement = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    four57b_retirement = models.DecimalField(max_digits=10, decimal_places=2,
                                             default=Decimal('0.00'))
    four01k_retirement = models.DecimalField(max_digits=10, decimal_places=2,
                                             default=Decimal('0.00'))
    roth_retirement = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    # Investment contributions
    robinhood_investments = models.DecimalField(max_digits=10, decimal_places=2,
                                                default=Decimal('0.00'))
    schwab_investments = models.DecimalField(max_digits=10, decimal_places=2,
                                             default=Decimal('0.00'))

    # Savings contributions
    amex_savings = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    fifththird_savings = models.DecimalField(max_digits=10, decimal_places=2,
                                             default=Decimal('0.00'))
    capone_savings = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    five29_college = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    huntington_savings = models.DecimalField(max_digits=10, decimal_places=2,
                                             default=Decimal('0.00'))

    # Taxes
    federal_tax = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    social_security = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    medicare = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    ohio_tax = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    columbus_tax = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    # Benefits/deductions
    health_insurance = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    supplementallife_insurance = models.DecimalField(max_digits=10, decimal_places=2,
                                                     default=Decimal('0.00'))
    flex_spending = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    cdm_std = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    cdmsupplemental_ltd = models.DecimalField(max_digits=10, decimal_places=2,
                                              default=Decimal('0.00'))
    parking = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    parking_admin = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    # Housing expenses
    main_mortgage = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    hoa_fees = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    # Insurance
    auto_insurance = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    # Utilities
    aep_electric = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    rumpke_trash = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    delaware_sewer = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    delco_water = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    suburban_gas = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    verizon_kat = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    sprint_justin = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    directtv_cable = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    timewarner_internet = models.DecimalField(max_digits=10, decimal_places=2,
                                              default=Decimal('0.00'))

    # Loan payments
    caponeauto_loan = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    public_loan = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    private_loan = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    # Credit card payments
    capone_creditcard = models.DecimalField(max_digits=10, decimal_places=2,
                                            default=Decimal('0.00'))
    amex_creditcard = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    discover_creditcard = models.DecimalField(max_digits=10, decimal_places=2,
                                              default=Decimal('0.00'))
    kohls_vicsec_macy_eddiebauer_creditcards = models.DecimalField(max_digits=10, decimal_places=2,
                                                                   default=Decimal('0.00'))
    katwork_creditcard = models.DecimalField(max_digits=10, decimal_places=2,
                                             default=Decimal('0.00'))

    # Other expenses
    cashorcheck_purchases = models.DecimalField(max_digits=10, decimal_places=2,
                                                default=Decimal('0.00'))
    daycare = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    taxdeductible_giving = models.DecimalField(max_digits=10, decimal_places=2,
                                               default=Decimal('0.00'))

    class Meta:
        ordering = ['-date']
        verbose_name = 'Monthly Income'
        verbose_name_plural = 'Monthly Income'
        db_table = 'Finance_monthinc'  # Match existing table name

    def __str__(self):
        return f"Income {self.date.strftime('%B %Y')}"

    # Income calculations
    def total_interest(self):
        return (self.huntington_interest + self.fifththird_interest +
                self.capone_interest + self.amex_interest + self.schwab_interest)

    def total_salary(self):
        return self.supremecourt_salary + self.cdm_salary

    def total_other_income(self):
        return (self.expense_checks + self.miscellaneous_income +
                self.refund_rebate_repayment + self.gift_income)

    def total_income(self):
        return (self.total_interest() + self.schwab_dividends +
                self.total_other_income() + self.total_salary())

    # Savings/investment calculations
    def total_retirement_contributions(self):
        return (self.opers_retirement + self.four57b_retirement +
                self.four01k_retirement + self.roth_retirement)

    def total_investment_contributions(self):
        return self.robinhood_investments + self.schwab_investments

    def total_savings_contributions(self):
        return (self.amex_savings + self.fifththird_savings +
                self.capone_savings + self.five29_college + self.huntington_savings)

    def total_allsavings(self):
        return (self.total_retirement_contributions() +
                self.total_investment_contributions() +
                self.total_savings_contributions())

    # Tax calculations
    def total_taxes(self):
        return (self.federal_tax + self.social_security + self.medicare +
                self.ohio_tax + self.columbus_tax)

    # Expense calculations
    def total_utilities(self):
        return (self.aep_electric + self.rumpke_trash + self.delaware_sewer +
                self.delco_water + self.suburban_gas + self.verizon_kat +
                self.sprint_justin + self.directtv_cable + self.timewarner_internet)

    def total_loans(self):
        return self.caponeauto_loan + self.public_loan + self.private_loan

    def total_personal_creditcards(self):
        return (self.capone_creditcard + self.amex_creditcard +
                self.discover_creditcard + self.kohls_vicsec_macy_eddiebauer_creditcards +
                self.katwork_creditcard)

    def total_housing(self):
        return self.main_mortgage + self.hoa_fees

    def total_benefits(self):
        return (self.health_insurance + self.supplementallife_insurance +
                self.flex_spending + self.cdm_std + self.cdmsupplemental_ltd +
                self.parking + self.parking_admin)

    def total_expenses(self):
        return (self.total_taxes() + self.total_utilities() + self.total_loans() +
                self.total_personal_creditcards() + self.total_housing() +
                self.total_benefits() + self.auto_insurance +
                self.cashorcheck_purchases + self.daycare + self.taxdeductible_giving)

    def total_surplus(self):
        return self.total_income() - self.total_expenses() - self.total_allsavings()


class TaxReturn(models.Model):
    """Annual tax return summary."""

    year = models.DateField()
    total_job_wages = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    total_federal_wages = models.DecimalField(max_digits=10, decimal_places=2,
                                              default=Decimal('0.00'))
    total_income = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    adjusted_gross_income = models.DecimalField(max_digits=10, decimal_places=2,
                                                default=Decimal('0.00'))
    itemized_deduction_total = models.DecimalField(max_digits=10, decimal_places=2,
                                                   default=Decimal('0.00'))
    federal_taxable_income = models.DecimalField(max_digits=10, decimal_places=2,
                                                 default=Decimal('0.00'))
    total_federal_tax_owed = models.DecimalField(max_digits=10, decimal_places=2,
                                                 default=Decimal('0.00'))
    total_federal_payments = models.DecimalField(max_digits=10, decimal_places=2,
                                                 default=Decimal('0.00'))
    state_taxable_income = models.DecimalField(max_digits=10, decimal_places=2,
                                               default=Decimal('0.00'))
    total_state_tax_owed = models.DecimalField(max_digits=10, decimal_places=2,
                                               default=Decimal('0.00'))
    total_state_payments = models.DecimalField(max_digits=10, decimal_places=2,
                                               default=Decimal('0.00'))

    class Meta:
        ordering = ['-year']
        verbose_name = 'Tax Return'
        verbose_name_plural = 'Tax Returns'
        db_table = 'Finance_taxreturn'  # Match existing table name

    def __str__(self):
        return f"Tax Return {self.year}"

    def federal_refund(self):
        return self.total_federal_payments - self.total_federal_tax_owed

    def state_refund(self):
        return self.total_state_payments - self.total_state_tax_owed

    def total_refund(self):
        return self.federal_refund() + self.state_refund()


class MetricConstants(models.Model):
    """Date/value pairs for financial metrics."""

    date = models.DateField()
    value = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    class Meta:
        verbose_name = 'Metric Constant'
        verbose_name_plural = 'Metric Constants'
        db_table = 'Finance_metricconstants'  # Match existing table name

    def __str__(self):
        return f"Metric {self.date}: {self.value}"
