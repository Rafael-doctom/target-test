# This program prints info about a business with data from a dictionary

# Putting data into a dictionary
faturamento_por_estado = dict()
faturamento_por_estado = {
    'sao_paulo': 67836.43,
    'rio_de_janeiro': 36678.66,
    'minas_gerais': 29229.88,
    'espirito_santo': 27165.48,
    'outros_estados': 19849.53,
}

# Getting total invoice
faturamento_total = 0
for key, value in faturamento_por_estado.items():
    faturamento_total = faturamento_total + value

# Getting percentages
for key, value in faturamento_por_estado.items():
    percentual_do_estado = (value / faturamento_total) * 100
    percentual_do_estado = "{:.2f}".format(percentual_do_estado)
    print(f'O percentual de representação de {key} dentro do faturamento total é {percentual_do_estado}%')
