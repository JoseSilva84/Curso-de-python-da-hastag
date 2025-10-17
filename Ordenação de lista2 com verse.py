produtos = ['televisão', 'notebook', 'smartphone', 'tablet', 'macbook', 'smart tv']
vendas = [1000, 2800, 1800, 1400, 13000, 2400]

#ordenar uma lista com o método sort(reverse=true)

vendas.sort(reverse=True)
print(vendas)

# O USO DO . JOIN() MAIS O "\N" QUE É O QUEBRA DE TEXTO
print('\n' .join(produtos))