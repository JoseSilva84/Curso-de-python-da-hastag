produtos = ['tv', 'celular', 'mouse']
item_usuario = input('Qual item deseja remove? ')
try:
    produtos.remove(item_usuario)
    print(produtos)
except:
    print(f'O produto {item_usuario} não existe na lista')