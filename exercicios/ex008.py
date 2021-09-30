print('Bem vindo ao conversor de medidas')
nome = input('Digite seu nome: ')
m = float(input('Digite sua altura em metros: '))
print('{} sua altura em centimetros é de {}cm,\n e em '
      'milimetros é de {}mm'.format(nome,m*100,m*1000))
