palavras = ('Amazonia', 'Chuveiro', 'Guitarra', 'Teclado', 'Computador', 'Vingadores', 'Bruxa', 'Visão')
for palavra in palavras:
    print(f'\nNa palavra \033[34m{palavra}\033[m temos as vogais ',end='')
    for vogal in palavra.lower():
        if vogal in 'aeiou':
            print(vogal, end=' ')
