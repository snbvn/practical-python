# report.py
#
# Exercise 2.4
import csv
portfolio=[]
def read_portfolio(filename):
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            stock = {
                'name'   : row[0],
                'shares' : int(row[1]),
                'price'   : float(row[2])
                }
            portfolio.append(stock)
    return portfolio

def read_prices(filename):
    prices={}             
    import csv         
    f=open(filename,'r')
    rows=csv.reader(f)
    for row in rows:
        try:
            prices[row[0]]=float(row[1])
        except IndexError:
            pass
    return prices
portfolio = read_portfolio('Data/portfolio.csv')
prices    = read_prices('Data/prices.csv')
totalcost=0
totalvalue=0
for i in portfolio:
    totalcost += i['shares']*i['price']
print('Total Cost:', totalvalue)
for shares in portfolio:
    totalvalue += prices[shares['name']] *shares['shares']
print('Current Value:', totalvalue)
print ('Gain:',totalvalue-totalcost)

def make_report(portfolio,prices):
    reporttuple=[]
    for i in portfolio:
        row = (i['name'], i['shares'], prices[i['name']],(prices[i['name']]-i['price']))
        reporttuple.append(row)
    return reporttuple  
report = make_report(portfolio,prices)  
header = ('Name', 'Shares', 'Price', 'Change')
print(f'{header[0]:>10s} {header[1]:>10s} {header[2]:>10s} {header[3]:>10s}')
print(f'{"-"*10:>10s} {"-"*10:>10s} {"-"*11:>11s} {"-"*10:>10s}')
#print('%10s %10s %10s %10s' % header)
#print(('-' * 10 + ' ') * 4)
for row in report:
    print(f'{ row[0]:>10s} {row[1]:>10d} {f"${row[2]:.2f}":>10} {row[3]:>10.2f}')