lista = []
pares = []
impares = []
for c in range(1, 8):
    numero = int(input(f'Digite o {c}º valor: '))
    if numero % 2 == 0 and numero > 0:
        pares.append(numero)
    elif numero % 2 == 1:
        impares.append(numero)
pares.sort()
impares.sort()
lista.append(pares)
lista.append(impares)

print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores impares digitados foram: {lista[1]}')