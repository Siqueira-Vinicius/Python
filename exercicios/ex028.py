import random
print('Jogando com os numeros')
print('O computador pensou em um numero entre 0 e 5,'
      'tende adivinhar!')
n = int(random.randint(0, 5))
j = int(input('Digite o seu palpite: '))
if j == n:
    print('Você Acertou!!!!')
else:
    print('Você Errou, o numero era {}!!!'.format(n))



