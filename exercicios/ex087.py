matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
somapar = c = somaterce = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matrix[linha][coluna] = int(input(f'Digite o valor na posição [{linha}, {coluna}]: '))

for elementos in matrix:
    print(elementos)

while c < 3:
    for elementos in matrix[c]:
        if elementos > 0 and elementos % 2 == 0:
            somapar += elementos

    somaterce += matrix[c][2]
    c += 1

print(f'A soma dos valores pares digitados é {somapar}')
print(f'A soma dos valores na terceira coluna é {somaterce}')
print(f'O maior valor da segunda linha é {max(matrix[1])}')


