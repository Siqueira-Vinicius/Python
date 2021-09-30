print('Maior e Menor')
n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
n3 = float(input('Digite um ultimo valor: '))
if n1 > n2:
    if n1 > n3:
        print('O maior valor é {}'.format(n1))
        if n2 > n3:
            print('O menor valor é {}'.format(n3))
        else:
            print('O menor valor é {}'.format(n2))
    else:
        print('O maior valor é {}'.format(n3))
        print('O menor valor é{}'.format(n2))
else:
    if n2 > n3:
        print('O maior valor é {}'.format(n2))
        if n1 > n3:
            print('O menor valor é {}'.format(n3))
        else:
            print('O menor valor é {}'.format(n1))
    else:
        print('O maior valor é {}'.format(n3))
        print('O menor valor é {}'.format(n1))

