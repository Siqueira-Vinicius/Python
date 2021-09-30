soma = quantidade = 0
while True:
    numero = int(input('Digite um numero: '))
    if numero == 999:
        break
    soma += numero
    quantidade += 1
print(f'Até digitar 999 voce digitou {quantidade} numeros e a soma entre eles foi de {soma}')

