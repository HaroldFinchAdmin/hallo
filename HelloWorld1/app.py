import openpyxl as xl

wb = xl.load_workbook('transactions.xlsx')

wb['Sheet1']
