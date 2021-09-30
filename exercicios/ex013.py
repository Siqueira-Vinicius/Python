print('Aumento para funcionarios')
s = float(input('Digite o salário atual '
                'do funcionario: R$'))
a = float(input('Digite a porcentagem do aumento: %'))
print('O salário do funcionario será de '
      'R${} reais.'.format(s+(s*a/100)))

