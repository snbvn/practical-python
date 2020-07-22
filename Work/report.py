
import csv
import fileparse
def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    return fileparse.parse_csv(filename, select=['name','shares','price'], types=[str,int,float])

def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    return dict(fileparse.parse_csv(filename,types=[str,float], has_headers=False))

def make_report(portfolio,prices):
    reporttuple=[]
    for i in portfolio:
        row = (i['name'], i['shares'], prices[i['name']],(prices[i['name']]-i['price']))
        reporttuple.append(row)
    return reporttuple  

def print_report(report):
    '''
    Print a nicely formated table from a list of (name, shares, price, change) tuples.
    '''
    header = ('Name', 'Shares', 'Price', 'Change')
    print(f'{header[0]:>10s} {header[1]:>10s} {header[2]:>10s} {header[3]:>10s}')
    print(f'{"-"*10:>10s} {"-"*10:>10s} {"-"*11:>11s} {"-"*10:>10s}')
    #print('%10s %10s %10s %10s' % header)
    #print(('-' * 10 + ' ') * 4)
    for row in report:
        print(f'{ row[0]:>10s} {row[1]:>10d} {f"${row[2]:.2f}":>10} {row[3]:>10.2f}')

def portfolio_report(portfoliofile,pricefile):        
    '''
    Make a stock report given portfolio and price data files.
    '''
    # Read data files 
    portfolio = read_portfolio(portfoliofile)
    prices    = read_prices(pricefile)

    # Create the report data
    report = make_report(portfolio,prices)

    # Print it out
    print_report(report)

portfolio_report('Data/portfolio.csv','Data/prices.csv')

def main(args):
    if len(args) != 3:
        raise SystemExit('Usage: %s portfile pricefile' % args[0])
    portfolio_report(args[1], args[2])

if __name__ == '__main__':
    import sys
    main(sys.argv)
'''
totalcost=0
totalvalue=0
for i in portfolio:
    totalcost += i['shares']*i['price']
print('Total Cost:', totalvalue)
for shares in portfolio:
    totalvalue += prices[shares['name']] *shares['shares']
print('Current Value:', totalvalue)
print ('Gain:',totalvalue-totalcost)
'''