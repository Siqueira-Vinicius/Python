# baixar moeda.py e armazenar na mesma pasta desse arquivo
import moeda
p = float(input(f'Digite um preço: {moeda.preço(formatar=True)}'))
a = int(input('Qual o valor do acrescimo?: %'))
d = int(input('Qual o valor do desconto?: %'))
f = moeda.formatar()
moeda.resumo(p, a, d, f)
