print('Bem vindo ao Calculador de Média Escolar')
nome = input('Digite o nome do aluno: ')
n1 = float(input('Digite a nota de {} no primeiro'
                 ' bimestre: '.format(nome)))
n2 = float(input('Digite a nota de {} no segundo'
                 ' bimestre: '.format(nome)))
n3 = float(input('Digite a nota de {} no terceiro'
                 'bimestre: '.format(nome)))
n4 = float(input('Digite a nota de {} no quarto '
                 'bimestre: '.format(nome)))
m = (n1+n2+n3+n4)/4
print('A média escolar de {} esse ano é de '
      ': {:.1f}'.format(nome,m))
