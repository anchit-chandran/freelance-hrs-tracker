HOURLY_RATE = 25

EXPENSES = 500
TAX_RATE = 0.2

PERSONAL_ALLOWANCE_YEARLY = 12570
PERSONAL_ALLOWANCE_MONTHLY = round(PERSONAL_ALLOWANCE_YEARLY / 7, 2)


def calculate_takehome(total_hrs: float) -> dict:
    gross_income = HOURLY_RATE * total_hrs
    gross_profit = gross_income - EXPENSES
    tax_amount = gross_profit * TAX_RATE
    take_home = gross_profit - tax_amount

    return {
        'HOURLY_RATE' : HOURLY_RATE,
        'EXPENSES' : EXPENSES,
        'PERSONAL_ALLOWANCE_MONTHLY' : PERSONAL_ALLOWANCE_MONTHLY,
        'gross_income' : gross_income,
        'gross_profit' : gross_profit,
        'tax_amount' : tax_amount,
        'take_home' : take_home,
    }
