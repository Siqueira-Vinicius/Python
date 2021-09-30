import moeda
p = float(input(f'Digite um preço: {moeda.preço()}'))
print(f'a metade de {moeda.preço(p)} é {moeda.metade(p)}')
print(f'o dobro de {moeda.preço(p)} é {moeda.dobro(p)}')
print(f'o preço de {moeda.preço(p)} reduzido em 10% é {moeda.desconto(p)}')
print(f'e o preço de {moeda.preço(p)} aumentado em 13% é {moeda.juros(p)}')
