# mortgage.py
#
# Exercise 1.7


principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month=0
new_payment = 3684.11
while principal > 0:
	if month < 12: # First 12 months with extra payment
		principal = principal * (1+rate/12) - new_payment
		total_paid = total_paid + new_payment
	else: # Regular payment after 12 months
		principal = principal * (1+rate/12) - payment
		total_paid = total_paid + payment
	month = month + 1
	
	# Final Adjustment if the principal goes negative
	if principal < 0:
		total_paid = total_paid + principal # Adjust the last payment
		principal = 0 # Set principal to 0 to exit the loop
print("Total Paid: ", round(total_paid, 2))
print("Months spent:", month)

