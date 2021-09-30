from utilitarios import moeda
from utilitarios import dados
dados.titulo(' Programa do Vinicius ', 2, '-')
p = dados.leiadinheiro(f'{dados.topico()} Digite um preço: {moeda.preço(formatar=True)}')
a = int(input(f'{dados.topico()} Qual o valor do acrescimo?: %'))
d = int(input(f'{dados.topico()} Qual o valor do desconto?: %'))
f = moeda.formatar()
moeda.resumo(p, a, d, f)
