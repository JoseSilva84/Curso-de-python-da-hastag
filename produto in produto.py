funcionarios = ['Wendel', 'Ítalo', 'Leo', 'Danilo', 'Amon'] 
cadeiras = ['veneza', 'letícia', 'banqueta', 'centro comum']

funcionario = input('Insira o nome do funcionário: ')
funcionario = funcionario.capitalize()
if funcionario in funcionarios:
    i = funcionarios.index(funcionario)
    cadeira_estoque = cadeiras[i]
    print(f'Temos a cadeira {cadeira_estoque} com {funcionario}')
else:
    print(f'{funcionario} não está na equipe de colaboradores')