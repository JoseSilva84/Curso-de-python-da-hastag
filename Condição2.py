nota = float(input('Digite sua nota: '))

if nota >= 7:
    print('Aprovado')
else:
    if nota >= 5:
        print('Não aprovado/Recuperação')
    else:
        print('naão aprovado/Reprovado direto')