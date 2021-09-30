print('É da familia Silva?')
nome = str(input('Qual é o seu nome completo?: '))
nome = nome.strip()
nome = nome.upper()
silva = 'SILVA' in nome
print('Você pertence a familia Silva?')
print('R:{}'.format(silva))
