primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
print('{}, '.format(primeiro), end='')
proximo = primeiro
c = 1
d = 9
h = 1
while h > 0:
    while c < d+1:
        proximo += razao
        print('{}, '.format(proximo), end='')
        c += 1
    print('Fim')
    h = int(input('\nquantos termos da PA a mais voce quer ver?(digite 0 para encerrar o programa): '))
    d += h

