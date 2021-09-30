matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for linha in range(0, 3):
    for coluna in range(0, 3):
        matrix[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))

for linhas in range(0, 3):
    for colunas in range(0, 3):
        print(f'[{matrix[linhas][colunas]:^5}]', end=' ')
    print()