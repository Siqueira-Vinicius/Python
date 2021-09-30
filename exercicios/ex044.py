from random import choice
from time import sleep
cores = {'limpa': '\033[m',
         'titulo': '\033[1;4;35m',
         'preto': '\033[30m',
         'azul': '\033[34m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'ciano': '\033[36m',
         'roxo': '\033[35m',
         'cinza': '\033[37m',
         'inverso': '\033[7m'}

cor = ['amarelo', 'azul', 'preto', 'vermelho', 'ciano', 'roxo', 'cinza', 'verde']

print('{}{:^39}{}'.format(cores['titulo'], 'MAGAZINE VINICIUS', cores['limpa']))
nome = str(input('Nome do Produto: ')).strip().title()
produto = float(input('Valor do {}{}{}: {}R${}'.format(cores[choice(cor)], nome,
                                                       cores['limpa'], cores['verde'], cores['limpa'])))

pagamento = int(input('Qual será a forma de pagamento?\n[1]{}Dinheiro{}/{}Cheque{}\n[2]{}Cartão{}\nR: '
                      .format(cores[choice(cor)], cores['limpa'], cores[choice(cor)],
                              cores['limpa'], cores[choice(cor)], cores['limpa'])))

if pagamento == 1:
    print('Pague {}R${}{:.2f} ao Caixa!'.format(cores['verde'], cores['limpa'], produto-(produto*(10/100))))
elif pagamento == 2:
    tipo = int(input('Débito ou Crédito?\n[1]{}Débito{}\n[2]{}Crédito {}\nR: '
                      .format(cores[choice(cor)], cores['limpa'], cores[choice(cor)], cores['limpa'])))
    if tipo == 1:
        print('Insira o cartão na máquina...')
        sleep(3)
        print('Preço:{}R${}{:.2f}'.format(cores['verde'], cores['limpa'], produto - (produto * (5 / 100))))
        senha = input('{}Senha{}: '.format(cores[choice(cor)], cores['limpa']))
        print('Verificando...')
        sleep(3)
        print('{}Compra Aprovada!{}'.format(cores['verde'], cores['limpa']))
    elif tipo == 2:
        vezes = int(input('Quantidade de parcelas\n[1]{}2x{}\n[2]{}3x ou mais{}\nR: '
                          .format(cores[choice(cor)], cores['limpa'], cores[choice(cor)], cores['limpa'])))
        if vezes == 1:
            print('Insira o cartão na máquina...')
            sleep(3)
            print('Preço:{}R${}{:.2f} (2 Parcelas de {}R${}{:.2f})'.format(cores['verde'], cores['limpa'], produto,
                                                                        cores['verde'], cores['limpa'], produto/2))
            senha = input('{}Senha{}: '.format(cores[choice(cor)], cores['limpa']))
            print('Verificando...')
            sleep(3)
            print('{}Compra Aprovada!{}'.format(cores['verde'], cores['limpa']))
        elif vezes == 2:
            vezes2 = int(input('Em quantas vezes deseja parcelar?(Max.12x): '))
            produto2 = produto + ((vezes2 - 2) * (produto * (5 / 100)))
            if 13 > vezes2 > 2:
                print('Insira o cartão na máquina...')
                sleep(3)
                print('Preço:{}R${}{:.2f} ({} Parcelas de {}R${}{:.2f})'.format(cores['verde'], cores['limpa'], produto2,
                                                                             vezes2, cores['verde'], cores['limpa'], produto2/vezes2))
                senha = input('{}Senha{}: '.format(cores[choice(cor)], cores['limpa']))
                print('Verificando...')
                sleep(3)
                print('{}Compra Aprovada!{}'.format(cores['verde'], cores['limpa']))
            else:
                print('{}Quantidade de parcelas Inválida!{}'.format(cores['inverso'], cores['limpa']))
        else:
            print('{}Opção Inválida!{}'.format(cores['inverso'], cores['limpa']))
    else:
        print('{}Opção Inválida!{}'.format(cores['inverso'], cores['limpa']))
else:
    print('{}Forma de Pagamento Inválida!{}'.format(cores['inverso'], cores['limpa']))

