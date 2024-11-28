# pcost.py
#
# Exercise 1.27
import csv
each_share = 0.0
shares = 0.0
prices = 0.0
total_cost = 0
with open('/Users/doston_ra/practical-python/Work/Data/portfolio.csv', 'rt') as file:
    reader = csv.reader(file)
    next(reader)
    for line in reader: 

        shares=  float(line[1])
        prices = float(line[2])
        each_share = shares * prices
        total_cost += each_share

print('Total cost is ', total_cost)

    
