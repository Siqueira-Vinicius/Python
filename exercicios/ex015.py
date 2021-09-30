print('Calcular Valor do Aluguel de carro')
d = int(input('Por quantos dias você alugou '
              'o carro?: '))
k = float(input('Quantos kilometros você rodou?: '))
print('O valor do aluguel do carro é '
      'de R${:.2f} reais.'.format(d*60+k*0.15))
