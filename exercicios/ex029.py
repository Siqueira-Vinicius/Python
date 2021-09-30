print('Seguindo as regras')
print('Você possui um carro, e esta apostando '
      'uma corrida')
v = float(input('Qual a velocidade '
                'maxima que seu carro chegou?(km/h): '))
if v > 80:
    print('Você excedeu a velocidade limite '
          'e foi pego no radar')
    print('Pague R${}'.format((v-80)*7))
if 80 >= v >= 70:
    print('Você foi o mais rapido e '
          'Venceu a Corrida!!!')
    print('Receba R$1 000 000,00')
if v < 70:
    print('Você foi muito lento e perdeu a corrida')
    print('Pague R$1 000 000,00 '
        '\ne entregue seu carro ao vencedor')



