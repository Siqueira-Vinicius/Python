cores = {'limpa':'\033[m',
         'titulo':'\033[1;4;35m',
         'azul':'\033[34m',
         'verde':'\033[32m',
         'vermelho':'\033[31m',
         'grifado':'\033[4m'}

print('{}Hexadecimal, Binario ou Octual{}'.format(cores['titulo'],cores['limpa']))
n = int(input('Digite um numero: '))
t = int(input('Você deseja transforma-lo em:\n[1]{}Binario{}\n[2]{}Hexadecimal{}\n[3]{}Octual{}\nR: '
              .format(cores['vermelho'],cores['limpa'],cores['azul'],cores['limpa'],cores['verde'],cores['limpa'])))
if t == 1:
    b = str(bin(n))
    print('O numero {} em {}Binario{} é {}{}{}'.format(n, cores['vermelho'],cores['limpa'],cores['grifado'], b[2:],cores['limpa']))
elif t == 2:
    h = str(hex(n))
    print('O numero {} em {}Hexadecimal{} é {}{}{}'.format(n,cores['azul'],cores['limpa'],cores['grifado'],h[2:],cores['limpa']))
elif t == 3:
    o = str(oct(n))
    print('O numero {} em {}Octual{} é {}{}{}'.format(n,cores['verde'],cores['limpa'],cores['grifado'],o[2:],cores['limpa']))
else:
    print('{}Opção Inválida!{}'.format('\033[7m', cores['limpa']))
