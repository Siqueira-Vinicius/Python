import math
print('Seno , Coseno e Tangente')
a = float(input('Digite o valor do Angulo  α:'))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('O seno de {} é {:.2f}'.format(a, s))
print('O coseno de {} é {:.2f}'.format(a, c))
print('A tangente de {} é {:.2f}'.format(a, t))



