import csv
import gzip
def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False, is_zip=False):
    '''
    Parse a CSV file.
    '''
    if is_zip:
        lines= gzip.open(filename, 'rt')
    else:
        lines= open(filename)

                  
    if select and not has_headers:
        raise RuntimeError('column headers')

    rows = csv.reader(lines, delimiter=delimiter)

    # file headers 
    headers = next(rows) if has_headers else []

    # If specific columns have been selected, make indices for filtering and set output columns
    if select:
        indices = [ headers.index(colname) for colname in select ]
        headers = select

    records = []
    for rowno, row in enumerate(rows, 1):
        if not row:     # Skip rows with no data
            continue

        # pick column 
        if select:
            row = [ row[index] for index in indices]

        # Apply type conversion to the row
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    print(f"Row {rowno}: Couldn't convert {row}")
                    print(f"Row {rowno}: Reason {e}")
                continue

        # Make a dictionary or a tuple
        if headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)

    return records
