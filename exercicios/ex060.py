
n = int(input('Digite um numero: '))
c = n-1
fatorial = n
print('{}! = {}'.format(n, n), end='')
while c > 0:
    fatorial *= c
    print('x{}'.format(c), end='')
    c -= 1
print(' = {}'.format(fatorial))
