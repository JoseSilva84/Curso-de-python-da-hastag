faturamento = input('Qual foi o faturamento da loja nesse Mês? ')
custo = input('Qual foi o custo da loja nesse mês? ')

if faturamento !='' and custo !='':
    lucro = int(faturamento) - int(custo)
    print(f'O lucro da loja foi {lucro:.2f} reais')
else:
    print('Algum valor não foi fornecido')