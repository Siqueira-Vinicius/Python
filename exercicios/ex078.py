lista = list()
for c in range(1, 6):
    lista.append(int(input(f'Digite o {c}º valor: ')))
print(lista)
print(f'O maior valor digitado foi o {max(lista)} digitado na ',end='')
for n, valores in enumerate(lista):
    if max(lista) == valores:
        print(n+1,end='ª...')
print(' vez')
print(f'O menor valor digitado foi o {min(lista)} digitado na ',end='')
for n, valores in enumerate(lista):
    if min(lista) == valores:
        print(n+1,end='ª...')
print(' vez')
