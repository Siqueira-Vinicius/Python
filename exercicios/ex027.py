print('Nome e Sobrenome')
nome = str(input('Qual seu nome completo?: '))\
    .strip().title()
n = nome.split()
print('Seu primeiro nome é {}'.format(n[0]))
print('E seu sobrenome é {}'.format(n[len(n)-1]))

