# mortgage.py
#
# Exercise 1.7


principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0.0

#User-defined extra payment variables
extra_payment_start_month=61    # Extra payments start after 5 years (month 61)
extra_payment_end_month = 108   # Extra payments end after 4 years (month 108)
extra_payment = 1000			# Extra payment amount
while principal > 0:
	# Chack if the current month is within the extra payment period
	if extra_payment_start_month <= month < extra_payment_end_month:
		monthly_payment = extra_payment + payment
	else:
		monthly_payment = payment
	# Apply monthly interest and substract the payment
	principal = principal * (1+rate/12) - payment
	total_paid += monthly_payment
	month +=1
	# Final adjustment if the principal goes negative
	if principal < 0:
		total_paid = total_paid + principal # Adjust the last payment
		principal = 0 # Set principal to 0 to exit the loop
	print(f'Month: {month} vs   {total_paid}')
	

