primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
print('{}, '.format(primeiro), end='')
proximo = primeiro
c = 1
while c < 10:
    proximo += razao
    print('{}, '.format(proximo), end='')
    c += 1
print('Fim')