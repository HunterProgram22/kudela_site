from django.core.management.base import BaseCommand
from finance.models import MonthBal, MonthInc, TaxReturn
from decimal import Decimal
from datetime import date


class Command(BaseCommand):
    help = 'Load test data for Finance app'

    def handle(self, *args, **options):
        self.stdout.write('Loading test data...')

        # Clear existing data
        MonthBal.objects.all().delete()
        MonthInc.objects.all().delete()
        TaxReturn.objects.all().delete()

        # Create MonthBal records for 2023 and 2024
        balance_data = [
            # 2023
            {'date': date(2023, 1, 1), 'base_networth': 150000},
            {'date': date(2023, 2, 1), 'base_networth': 152000},
            {'date': date(2023, 3, 1), 'base_networth': 155000},
            {'date': date(2023, 4, 1), 'base_networth': 158000},
            {'date': date(2023, 5, 1), 'base_networth': 160000},
            {'date': date(2023, 6, 1), 'base_networth': 163000},
            {'date': date(2023, 7, 1), 'base_networth': 165000},
            {'date': date(2023, 8, 1), 'base_networth': 168000},
            {'date': date(2023, 9, 1), 'base_networth': 170000},
            {'date': date(2023, 10, 1), 'base_networth': 173000},
            {'date': date(2023, 11, 1), 'base_networth': 175000},
            {'date': date(2023, 12, 1), 'base_networth': 178000},
            # 2024
            {'date': date(2024, 1, 1), 'base_networth': 180000},
            {'date': date(2024, 2, 1), 'base_networth': 183000},
            {'date': date(2024, 3, 1), 'base_networth': 186000},
            {'date': date(2024, 4, 1), 'base_networth': 189000},
            {'date': date(2024, 5, 1), 'base_networth': 192000},
            {'date': date(2024, 6, 1), 'base_networth': 195000},
            {'date': date(2024, 7, 1), 'base_networth': 198000},
            {'date': date(2024, 8, 1), 'base_networth': 201000},
            {'date': date(2024, 9, 1), 'base_networth': 204000},
            {'date': date(2024, 10, 1), 'base_networth': 207000},
            {'date': date(2024, 11, 1), 'base_networth': 210000},
            {'date': date(2024, 12, 1), 'base_networth': 213000},
        ]

        for data in balance_data:
            base = data['base_networth']
            MonthBal.objects.create(
                date=data['date'],
                huntington_check=Decimal(base * 0.02),
                fifththird_check=Decimal(base * 0.01),
                huntington_save=Decimal(base * 0.03),
                fifththird_save=Decimal(base * 0.02),
                capone_save=Decimal(base * 0.05),
                amex_save=Decimal(base * 0.03),
                robinhood_invest=Decimal(base * 0.08),
                deacon_invest=Decimal(base * 0.05),
                buckeye_invest=Decimal(base * 0.03),
                opers_retire=Decimal(base * 0.15),
                four57_retire=Decimal(base * 0.10),
                four01_retire=Decimal(base * 0.12),
                roth_retire=Decimal(base * 0.08),
                main_home=Decimal(350000),
                justin_car=Decimal(25000),
                kat_car=Decimal(20000),
                capone_credit=Decimal(1500),
                amex_credit=Decimal(2000),
                discover_credit=Decimal(500),
                car_loan=Decimal(15000),
                pubstudent_loan=Decimal(10000),
                privstudent_loan=Decimal(5000),
                main_mortgage=Decimal(280000),
            )

        self.stdout.write(f'Created {len(balance_data)} MonthBal records')

        # Create MonthInc records
        income_data = [
            # 2023
            {'date': date(2023, 1, 1)},
            {'date': date(2023, 2, 1)},
            {'date': date(2023, 3, 1)},
            {'date': date(2023, 4, 1)},
            {'date': date(2023, 5, 1)},
            {'date': date(2023, 6, 1)},
            {'date': date(2023, 7, 1)},
            {'date': date(2023, 8, 1)},
            {'date': date(2023, 9, 1)},
            {'date': date(2023, 10, 1)},
            {'date': date(2023, 11, 1)},
            {'date': date(2023, 12, 1)},
            # 2024
            {'date': date(2024, 1, 1)},
            {'date': date(2024, 2, 1)},
            {'date': date(2024, 3, 1)},
            {'date': date(2024, 4, 1)},
            {'date': date(2024, 5, 1)},
            {'date': date(2024, 6, 1)},
            {'date': date(2024, 7, 1)},
            {'date': date(2024, 8, 1)},
            {'date': date(2024, 9, 1)},
            {'date': date(2024, 10, 1)},
            {'date': date(2024, 11, 1)},
            {'date': date(2024, 12, 1)},
        ]

        for data in income_data:
            MonthInc.objects.create(
                date=data['date'],
                huntington_interest=Decimal('5.25'),
                fifththird_interest=Decimal('3.10'),
                capone_interest=Decimal('45.00'),
                amex_interest=Decimal('35.00'),
                schwab_interest=Decimal('12.50'),
                schwab_dividends=Decimal('150.00'),
                supremecourt_salary=Decimal('4500.00'),
                cdm_salary=Decimal('5500.00'),
                opers_retirement=Decimal('450.00'),
                four57b_retirement=Decimal('400.00'),
                four01k_retirement=Decimal('500.00'),
                roth_retirement=Decimal('250.00'),
                robinhood_investments=Decimal('200.00'),
                schwab_investments=Decimal('300.00'),
                amex_savings=Decimal('200.00'),
                fifththird_savings=Decimal('100.00'),
                capone_savings=Decimal('150.00'),
                huntington_savings=Decimal('100.00'),
                federal_tax=Decimal('1200.00'),
                social_security=Decimal('620.00'),
                medicare=Decimal('145.00'),
                ohio_tax=Decimal('350.00'),
                columbus_tax=Decimal('200.00'),
                health_insurance=Decimal('450.00'),
                supplementallife_insurance=Decimal('25.00'),
                flex_spending=Decimal('100.00'),
                main_mortgage=Decimal('1850.00'),
                hoa_fees=Decimal('150.00'),
                auto_insurance=Decimal('180.00'),
                aep_electric=Decimal('120.00'),
                rumpke_trash=Decimal('35.00'),
                delaware_sewer=Decimal('45.00'),
                delco_water=Decimal('55.00'),
                suburban_gas=Decimal('85.00'),
                verizon_kat=Decimal('85.00'),
                sprint_justin=Decimal('75.00'),
                directtv_cable=Decimal('120.00'),
                timewarner_internet=Decimal('70.00'),
                capone_creditcard=Decimal('500.00'),
                amex_creditcard=Decimal('750.00'),
                discover_creditcard=Decimal('200.00'),
                cashorcheck_purchases=Decimal('300.00'),
            )

        self.stdout.write(f'Created {len(income_data)} MonthInc records')

        # Create TaxReturn records
        tax_years = [2021, 2022, 2023]

        for year in tax_years:
            TaxReturn.objects.create(
                year=date(year, 1, 1),
                total_job_wages=Decimal('120000.00'),
                total_federal_wages=Decimal('115000.00'),
                total_income=Decimal('125000.00'),
                adjusted_gross_income=Decimal('110000.00'),
                itemized_deduction_total=Decimal('25000.00'),
                federal_taxable_income=Decimal('85000.00'),
                total_federal_tax_owed=Decimal('14000.00'),
                total_federal_payments=Decimal('15500.00'),
                state_taxable_income=Decimal('105000.00'),
                total_state_tax_owed=Decimal('4200.00'),
                total_state_payments=Decimal('4500.00'),
            )

        self.stdout.write(f'Created {len(tax_years)} TaxReturn records')

        self.stdout.write(self.style.SUCCESS('Test data loaded successfully!'))
