import random
print('Orden de apresentação')
n1 = str(input('Digite o nome do aluno:'))
n2 = str(input('Digite o nome do aluno:'))
n3 = str(input('Digite o nome do aluno:'))
n4 = str(input('Digite o nome do aluno:'))
l = [n1, n2, n3, n4]
random.shuffle(l)
print('A ordem de apresentação é {}'
      .format(l))

