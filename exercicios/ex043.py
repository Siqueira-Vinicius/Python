cores = {'limpa': '\033[m',
         'titulo': '\033[1;4;35m',
         'preto': '\033[30m',
         'vermelho': '\033[31m',
         'azul': '\033[34m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'ciano': '\033[36m'}

print('{}Indice de Massa Corporea{}'.format(cores['titulo'], cores['limpa']))
peso = float(input('Qual o Seu Peso({}Kg{})?: '.format(cores['vermelho'], cores['limpa'])))
altura = float(input('Digite a Sua altura({}M{})?: '.format(cores['azul'], cores['limpa'])))
imc = peso/(altura**2)

if imc < 15:
    print('Seu Imc é {:.1f} Você está {}Desnutrido{}!'.format(imc, cores['ciano'], cores['limpa']))
elif 15 <= imc < 18.5:
    print('Seu Imc é {:.1f} Você está {}Abaixo do Peso{}!'.format(imc, cores['azul'], cores['limpa']))
elif 18.5 <= imc < 25:
    print('Seu Imc é {:.1f} Você está no seu {}Peso Ideal{}!'.format(imc, cores['verde'], cores['limpa']))
elif 25 <= imc < 30:
    print('Seu Imc é {:.1f} Você está {}Acima do Peso{}!'.format(imc, cores['amarelo'], cores['limpa']))
elif 30 <= imc < 40:
    print('Seu imc é {:.2f} Você está {}Obeso{}!'.format(imc, cores['vermelho'], cores['limpa']))
elif 40 <= imc:
    print('Seu imc é {:.2f} Você possui {}Obesidade Morbida{}!'.format(imc, cores['preto'], cores['limpa']))