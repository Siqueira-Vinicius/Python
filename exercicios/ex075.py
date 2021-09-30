tupla = (int(input('Digite o 1º numero: ')),
int(input('Digite o 2º numero: ')),
int(input('Digite o 3º numero: ')),
int(input('Digite o 4º numero: ')))
if 9 in tupla:
    if tupla.count(9) == 1:
        print(f'Você digitou o numero nove {tupla.count(9)} vez')
    else:
        print(f'Você digitou o numero nove {tupla.count(9)} vezes')
else:
    print(f'Você não digitou o numero nove nenhuma vez')

if 3 in tupla:
    print(f'O numero 3 foi digitado na {tupla.index(3)+1}ª vez')
else:
    print(f'O numero 3 não foi digitado nenhuma vez')

print('Os numeros pares digitados foram : ',end='')
for c in tupla:
    if 0 < c and c % 2 == 0:
        print(c,end=' ')
