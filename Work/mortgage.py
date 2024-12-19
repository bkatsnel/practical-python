# mortgage.py
principal = 500000.0
rate = 0.05
payment = 2684.11
extra_payment = 1000.0
total_paid = 0.0
months = 0

# First year with extra payments
for month in range(12):
    principal = principal * (1 + rate / 12) - (payment + extra_payment)
    total_paid += (payment + extra_payment)
    months += 1

# Remaining months without extra payments
while principal > 0:
    principal = principal * (1 + rate / 12) - payment
    total_paid += payment
    months += 1

print('Total paid:', total_paid)
print('Months required:', months)
