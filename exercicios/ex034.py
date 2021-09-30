print('AUmento 2.0')
salario = float(input('Digite o valor do seu salario: '))
if salario > 1250:
    print('Seu novo salario é {}'.format(salario+salario*10/100))
else:
    print('Seu novo salario é {}'.format(salario+salario*15/100))
