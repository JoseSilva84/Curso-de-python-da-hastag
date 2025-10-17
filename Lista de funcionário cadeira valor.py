funcionario = ['Leo', 'Ítalo', 'Geovane', 'Wendel', 'Danilo']
cadeira = ['letícia', 'veneza']
qtde_cadeira = [29, 20, 60, 80, 7]
valor_unitario = [7.00, 7.00, 7.00, 7.00, 7.00]
total_cadeira = sum(qtde_cadeira)
valor_cadeira = [a * b for a, b in zip(qtde_cadeira, valor_unitario)]
print(total_cadeira)
print(valor_cadeira)