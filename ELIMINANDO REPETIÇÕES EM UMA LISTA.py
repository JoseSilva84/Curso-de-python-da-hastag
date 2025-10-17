produtos = ['televisão', 'notebook', 'smartfone', 'tablet']
novos_produtos = ['smart tv', 'tablet']

mais_lista = produtos + novos_produtos

# forma que resolver uma lista com dados repetidos
mais_lista = list(set(mais_lista))
print(mais_lista)
