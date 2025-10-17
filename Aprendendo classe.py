def media_de_alunos(nota1, nota2):
    soma = nota1 + nota2
    media_total = nota1 + nota2
    return(soma, media_total)

print(media_de_alunos(8, 9))

def alunos():
    aluno = int(input('Quantos nomes  você quer adicionar? '))
    nome = []
    for estudante in range(aluno):
        receba_nome = input('Digite seu nome? ')
        nome.append(receba_nome)
    return(nome)
print(alunos())