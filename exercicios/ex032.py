print('Ano Bissexto')
ano = int(input('Digite o ano que deseja consultar: '))
if ano % 4 == 0:
    print('O ano de {} possui 336 dias'.format(ano))
    print('É um ano Bissexto')
else:
    print('O ano de {} possui 335 dias'.format(ano))
    print('Não é um ano Bissexto')