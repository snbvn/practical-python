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
            #row = line.split(',')
            portfolio.append ((row[0],int(row[1]),float(row[2])))
    return portfolio