numeros = 0
soma = 0
n = 0
while n != 999:
    n = int(input('Digite um numero: '))
    soma += n
    numeros += 1
soma -= 999
numeros -= 1
print('A soma dos {} numeros digitados foi {}'.format(numeros, soma))