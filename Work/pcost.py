# pcost.py
#
# Exercise 1.27
import sys
def portfolio_cost(filename): 
    price=0
    f = open(filename, 'rt')
    headers = next(f).split(',')
    
    for line in f:
        row = line.split(',')
        try:       
            price= price + int(row[1])* float(row[2])
        except ValueError:
            print("error")
    return price

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)