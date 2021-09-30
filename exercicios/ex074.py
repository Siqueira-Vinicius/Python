from random import randint
numeros = (randint(0, 100), randint(0,100), randint(0,100), randint(0,100), randint(0, 100))
print(f'Os valores sorteados foram: {numeros}')
print(f'O menor numero foi o {max(numeros)}')
print(f'O maior numero foi o {min(numeros)}')
