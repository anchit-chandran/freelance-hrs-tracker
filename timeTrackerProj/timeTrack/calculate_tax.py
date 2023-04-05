HOURLY_RATE = 25

EXPENSES = 250
TAX_RATE = 0.2

PERSONAL_ALLOWANCE_YEARLY = 12570
PERSONAL_ALLOWANCE_MONTHLY = round(PERSONAL_ALLOWANCE_YEARLY / 7, 2)

N1C4_LOWER_THRESHOLD = 11908
N1C4_LOWER_RATE = 0.0973

NIC2_AMOUNT = 3.15 * 52  # £3.15 per week


def calculate_takehome(total_hrs: float) -> dict:
    gross_income = HOURLY_RATE * total_hrs * 7
    gross_profit = gross_income - EXPENSES * 7
    taxable_income = gross_profit - PERSONAL_ALLOWANCE_YEARLY
    total_income_tax = TAX_RATE * taxable_income
    profit_after_tax = gross_profit - total_income_tax
    amount_due_NIC4 = gross_profit - N1C4_LOWER_THRESHOLD
    NIC4_amount = amount_due_NIC4 * N1C4_LOWER_RATE
    sum_NI_amount = NIC4_amount + NIC2_AMOUNT
    take_home = profit_after_tax - sum_NI_amount

    return {
        'YEARLY':
            {
                'gross_income': gross_income,
                'gross_profit': gross_profit,
                'taxable_income': taxable_income,
                'total_income_tax': total_income_tax,
                'profit_after_tax': profit_after_tax,
                'amount_due_NIC4': amount_due_NIC4,
                'NIC4_amount': NIC4_amount,
                'sum_NI_amount': sum_NI_amount,
                'take_home': take_home,
            },
        'MONTHLY':
            {
                'gross_income': gross_income/7,
                'gross_profit': gross_profit/7,
                'taxable_income': taxable_income/7,
                'total_income_tax': total_income_tax/7,
                'profit_after_tax': profit_after_tax/7,
                'amount_due_NIC4': amount_due_NIC4/7,
                'NIC4_amount': NIC4_amount/7,
                'sum_NI_amount': sum_NI_amount/7,
                'take_home': take_home/7,
            },
    }


print(calculate_takehome(160))
