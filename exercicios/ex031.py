print('preço da viagem')
d = float(input('Distancia da viagem em '
                'quilometros(km): '))
if d <= 200:
    print('O valor da sua passagem de avião é R${}'
          .format(d*0.5))
else:
    print('o valor da sua passagem de avião é R${}'
          .format(d*0.45))
