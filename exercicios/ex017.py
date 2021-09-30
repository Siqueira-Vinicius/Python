from math import sqrt, pow
print('Calculador de Hipotenusas Triangulo Retangulo')
co = float(input('Digite o valor do cateto oposto:'))
ca = float(input('Digite o valor do cateto adjascente:'))
h = sqrt(pow(ca,2) + pow(co,2))
print('A hipotenusa desse triangulo é {:.2f}'.format(h))
