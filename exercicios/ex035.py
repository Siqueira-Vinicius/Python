print('Pode formar um triangulo?')
r1 = float(input('Digite o valor de primeira reta: '))
r2 = float(input('DIgite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))
if r3 - r2 < 0:
    r4 = (r3 - r2)*-1
else:
    r4 = r3 - r2
if r4 < r1 < (r2+r3):
    print('É possivel formar um triangulo '
          'com as retas {},{} e {}'
          .format(r1, r2, r3))
else:
    print('Não é possivel formar um triangulo com as retas'
    ' {}, {} e {}'.format(r1,r2,r3))
