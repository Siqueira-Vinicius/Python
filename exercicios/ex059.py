from time import sleep
c = {'l': '\033[m', 'inverso': '\033[7m', 'az': '\033[34m', 'am': '\033[33m', 'vm': '\033[31m', 'vr': '\033[32m',
     'p': '\033[30m', 'rx': '\033[35m'}
n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
r = 0
while r != 5:
    print('{}{:^24}{}\n[1]{}Soma{}\n[2]{}Multiplicação{}\n[3]{}Maior{}\n[4]{}Novos Numeros{}\n[5]{}Sair do Programa{}'
          .format(c['rx'], 'Menu', c['l'], c['vr'], c['l'], c['vm'], c['l'], c['az'], c['l'], c['am'], c['l'],
                  c['p'], c['l']))

    r = int(input('R: '))
    if r < 1 or r > 5:
        print('{} Opção Inválida, Tente Novamente! {}'.format(c['inverso'], c['l']))
        sleep(3)
    elif r == 1:
        print('{} A soma entre {} e {} é igual a {} {}'.format('\033[42m', n1, n2, n1+n2, c['l']))
        sleep(3)
    elif r == 2:
        print('{} A multiplicação entre {} e {} é igual a {} {} '. format('\033[41m', n1, n2, n1*n2, c['l']))
        sleep(3)
    elif r == 3:
        if n1 > n2:
            print('{} O maior numero entre {} e {} é o numero {} {}'.format('\033[44m', n1, n2, n1, c['l']))
            sleep(3)
        elif n2 > n1:
            print('{} O maior Numero entre {} e {} é o numero {} {}'.format('\033[44m', n1, n2, n2, c['l']))
            sleep(3)
        else:
            print('{} Não há maior Numero entre {} e {} pois eles são iguais {}'.format('\033[44m', n1, n2, c['l']))
            sleep(3.5)
    elif r == 4:
        n1 = float(input('Digite um valor: '))
        n2 = float(input('Digite outro valor: '))
