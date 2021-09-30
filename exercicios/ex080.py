numeros = list()
s = 0
for c in range(1, 6):
    numero = int(input(f'Digite o {c}º valor: '))
    if c == 1 or numero > numeros[-1]:
        numeros.append(numero)
        print(f'O numero {numero} foi adicionado na {len(numeros)}ª posição')
    else:
        indice = 0
        while indice < len(numeros):
            if numero <= numeros[indice]:
                numeros.insert(indice, numero)
                print(f'O numero {numero} foi adicionado na {indice+1}ª posição')
                break
            indice +=1
print(f'Valores digitados em ordem crescente: {numeros}')