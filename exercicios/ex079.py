numeros = list()
contador = 1

while True:
    numero = int(input((f'Digite o {contador}º numero: ')))
    if numero not in numeros:
        numeros.append(numero)
    while True:
        continuar = input('Quer cadastrar mais algum numero?[S][N]: ')
        if continuar in 'SsNn':
            break
        else:
            print('Resposta Inválida, Tente Novamente!')
    if continuar in 'Nn':
        break
    contador += 1
numeros.sort()
print(f'Valores digitados em ordem crescente: {numeros}')

