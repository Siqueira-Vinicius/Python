print('par ou impar?')
n = int(input('Digite o numero que deseja verificar'
              'se é par ou impar: '))
if n % 2 == 0:
    print('O numero escolhido {} é um numero Par'
          .format(n))
if n % 2 != 0:
    print('O numero escolhido {} é um numero Impar'
          .format(n))
