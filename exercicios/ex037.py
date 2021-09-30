cores = {'limpa':'\033[m',
         'titulo':'\033[1;4;35m',
         'verde':'\033[32m',
         'vermelho':'\033[31m',
         'preto':'\033[1;30m',
         'azul':'\033[34m',
         'amarelo':'\033[33m'}


print('{}Emprestimo Bancario{}'.format(cores['titulo'],cores['limpa']))
casa = float(input('Digite o valor da {}casa{} que deseja financiar: {}R${}'.format(cores['azul'],cores['limpa'],cores['verde'],cores['limpa'])))
salario = float(input('Digite o valor do seu {}salario{} : {}R${}'.format(cores['amarelo'],cores['limpa'],cores['verde'],cores['limpa'])))
anos = int(input('Em quantos {}anos{} deseja pagar?: '.format(cores['vermelho'],cores['limpa'])))
if casa/(anos*12) > salario*(30/100):
    print('O Emprestimo foi {}NEGADO{}!'.format(cores['preto'],cores['limpa']))
else:
    print('O Emprestimo foi {}CONCEDIDO{}!'.format(cores['verde'],cores['limpa']))
    print('O valor da prestação mensal será de {}R${}{:.2f}'.format(cores['verde'],cores['limpa'], casa/(anos*12)))
