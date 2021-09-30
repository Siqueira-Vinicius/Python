tupla = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
         'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    numero = int(input('Digite um numero de 0 a 20: '))
    if 0 <= numero <= 20:
        break
    else:
        print('\033[7m Opção Inválida, Tente Novamente! \033[m')
resultado = f'\033[34m{tupla[numero]}\033[m'
print(f'Você digitou o numero {resultado}')


