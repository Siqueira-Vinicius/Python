print('Conversor de Temperatura')
c = float(input('Digite a temperatura em grau '
                'Celcius: ºC'))
print('A temperatura de {}ºC é equivalente a'
      ' {:.0f} K(kelvins) e\n'
      '{:.0f}ºF(graus Fahrenheit'
      ')'.format(c,c+274.15,(c*9/5)+32))
