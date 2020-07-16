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