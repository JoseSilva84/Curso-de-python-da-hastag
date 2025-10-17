meta = 20000
vendas = 25000
if vendas < meta:
    print('Não ganhou bônus')
elif vendas > meta:
    bonus = 0.08 * vendas
    print(f'Ganhou o bônus de R$ {bonus:.2f}')
else:
    bonus = 0.03 * vendas
    print(f'Ganhou o bônus de R$ {bonus:.2f}')