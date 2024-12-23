"""
mortgage.py
"""

PRINCIPAL = 500000.0
RATE = 0.05
PAYMENT = 2684.11
CURRENT_PAYMENT = 0.0
EXTRA_PAYMENT = 1000.0
EXTRA_PAYMENT_START_MONTH = 60
EXTRA_PAYMENT_END_MONTH = 108
TOTAL_PAID = 0.0
MONTHS_PAID = 0

def print_payment_history(months_paid, current_payment, total_payment, principal):
    """
    print_payment_history formats arguments, rounds each argument to two decimals
    and prints themt to the console.
    """
    print(
        round(months_paid, 2),
        round(current_payment, 2),
        round(total_payment, 2),
        round(principal, 2)
    )

while PRINCIPAL > 0:
    MONTHS_PAID = MONTHS_PAID + 1

    if PRINCIPAL < PAYMENT:
        CURRENT_PAYMENT = PRINCIPAL
        TOTAL_PAID = TOTAL_PAID + PRINCIPAL
        PRINCIPAL = 0
        break

    if EXTRA_PAYMENT_START_MONTH <= MONTHS_PAID <= EXTRA_PAYMENT_END_MONTH:
        CURRENT_PAYMENT = PAYMENT + EXTRA_PAYMENT
    else:
        CURRENT_PAYMENT = PAYMENT

    TOTAL_PAID = TOTAL_PAID + CURRENT_PAYMENT
    PRINCIPAL = PRINCIPAL * (1 + RATE / 12) - CURRENT_PAYMENT
    print_payment_history(MONTHS_PAID, CURRENT_PAYMENT, TOTAL_PAID, PRINCIPAL)

print_payment_history(MONTHS_PAID, CURRENT_PAYMENT, TOTAL_PAID, PRINCIPAL)
print('Total paid', round(TOTAL_PAID, 2))
print('Months paid', MONTHS_PAID)
