# This program prints info about a business with data from a JSON file

import json

# Opening json file
while True:
    try:
        file = open('dados.json')
        js = json.load(file)
        break
    except FileNotFoundError:
        print('File not found.')
        quit()

# Building a list with all invoice
invoice_lst = []
for i in range(len(js)):
    if float(js[i]['valor']) != 0:
        invoice_lst.append(float(js[i]['valor']))

# Setting up variables
max_invoice = invoice_lst[0]
min_invoice = invoice_lst[0]
avg_invoice = 0
total_invoice = 0
days_above_avg = 0


# Saving max invoice, min invoice and sum of all invoice
for value in range(len(invoice_lst)):
    if invoice_lst[value] >= max_invoice:
        max_invoice = invoice_lst[value]
    if invoice_lst[value] <= min_invoice:
        min_invoice = invoice_lst[value]
    total_invoice = total_invoice + invoice_lst[value]

# Getting average invoice
avg_invoice = total_invoice / len(invoice_lst)

# Getting total days above average
for value in range(len(invoice_lst)):
    if invoice_lst[value] > avg_invoice:
        days_above_avg += 1

print(f'The minimum invoice was {min_invoice}')
print(f'The maximum invoice was {max_invoice}')
print(f'Total days above average invoice: {days_above_avg}')
