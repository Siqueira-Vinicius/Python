print('Quantidade de tinta')
l = float(input('Digite a largura da parede(m): '))
a = float(input('Digite a altura da parede(m): '))
print('Para a área de {:.2f}m² são necessarios {:.2f}L '
      'de tinta.'.format(l*a,(l*a)/2))
