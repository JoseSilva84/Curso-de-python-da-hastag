meta_funcionario = 10000
meta_loja = 25000
vendas_funcionario = 15000
vendas_loja = 0

if vendas_funcionario > meta_funcionario and vendas_loja > meta_loja:
    bonus = 00.3 * vendas_funcionario
    print(f'Bônus do funcionário foi {bonus:.2f}')
else:
    print('Funcionário não ganhou bônus')