
cores = {'limpa':'\033[m',
         'titulo':'\033[1;4;35m',
         'azul':'\033[34m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'amarelo':'\033[33m',
         'preto':'\033[7m'}

print('{}Tipos de Triângulo{}'.format(cores['titulo'],cores['limpa']))
print('Digite o tamanho das 3 retas')
reta1 = float(input('Valor da {}primeira{} reta: '.format(cores['vermelho'], cores['limpa'])))
reta2 = float(input('Valor da {}segunda{} reta: '.format(cores['azul'], cores['limpa'])))
reta3 = float(input('Valor da {}terceira{} reta: '.format(cores['verde'], cores['limpa'])))

if (reta2-reta3) < 0:
    d1 = (reta2-reta3)*(-1)
else:
    d1 = (reta2-reta3)
if (reta1-reta3) < 0:
    d2 = (reta1-reta3)*(-1)
else:
    d2 = (reta1-reta3)
if (reta1-reta2) < 0:
    d3 = (reta1-reta2)*(-1)
else:
    d3 = (reta1-reta2)

if reta1 == reta2 == reta3:
    tipo = 'Equilátero'
elif reta1 != reta2 != reta3:
    tipo = 'Escaleno'
else:
    tipo = 'Isóceles'

if d1 < reta1 < (reta2+reta3) and d2 < reta2 < (reta1+reta3) and d3 < reta3 < (reta1+reta2):
    print('É possivel formar um triangulo {}{}{} com essas 3 retas!'.format(cores['amarelo'], tipo, cores['limpa']))
else:
    print('{}Não é possivel formar um triângulo com essas 3 retas!{}'.format(cores['preto'], cores['limpa']))


