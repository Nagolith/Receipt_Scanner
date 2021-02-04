import pandas as pd
import openpyxl

# converts txt file to cvs
read_file = pd.read_csv (r'/Users/jonathanhald/Documents/SAI/receipt_scanner/Receipt_Scanner/scanner.txt', sep='delimiter', header=None)
read_file.to_csv (r'/Users/jonathanhald/Documents/SAI/receipt_scanner/Receipt_Scanner/scanner.csv', index=None)

# converts cvs file to excel file
read_file = pd.read_csv (r'/Users/jonathanhald/Documents/SAI/receipt_scanner/Receipt_Scanner/scanner.csv')
read_file.to_excel (r'/Users/jonathanhald/Documents/SAI/receipt_scanner/Receipt_Scanner/scanner_excel.xlsx', index = None, header=True)
