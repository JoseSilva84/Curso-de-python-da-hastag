faturamento = input('Qual foi o faturamento da loja nesse Mês? ')
custo = input('Qual foi o custo da loja nesse mês? ')

lucro = int(faturamento) - int(custo)

print(f'O lucro da loja foi {lucro:.2f}')