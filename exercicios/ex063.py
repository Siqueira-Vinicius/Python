n = int(input('Digite um numero: '))
x = 0
fribo3 = 0
fribo1 = 0
fribo2 = 1
x = x+2
print('0, 1, ', end='')
while x < n:
    fribo3 = fribo1 + fribo2
    print('{}, '.format(fribo3), end='')
    fribo1 = fribo2
    fribo2 = fribo3
    x += 1
print('fim')