def leiaint(msg):
    while True:
        print(msg, end='')
        numero = input()
        if numero.isnumeric():
            return numero
        else:
            print('\033[31mERRO. Entrada inválida!\033[m')


n = leiaint('Digite um numero inteiro: ')
print(f'Voce acabou de digitar o numero {n}')