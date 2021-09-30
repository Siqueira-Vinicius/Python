listagem = ('Lapís', 1.50, 'Borracha', 3.75, 'Estojo', 5.99, 'Caderno', 15, 'Mochila', 123.89)

print('-'*40)
print(f'\033[34m{"lISTAGEM DE PREÇOS":^40}\033[m')
print('-'*40)

for itens in listagem[::2]:
    preco = listagem[listagem.index(itens)+1]
    print(f'{itens:.<30}\033[32mR$ \033[m{preco:>6.2f}')
print('-'*40)