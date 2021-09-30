import moeda
p = float(input('Digite um preço: \033[32mR$\033[m'))
print(f'a metade de \033[32mR$\033[m{p:.2f} é \033[32mR$\033[m{moeda.metade(p):.2f}')
print(f'o dobro de \033[32mR$\033[m{p:.2f} é \033[32mR$\033[m{moeda.dobro(p):.2f}')
print(f'o preço de \033[32mR$\033[m{p:.2f} reduzido em 10% é \033[32mR$\033[m{moeda.desconto(p):.2f}')
print(f'e o preço de \033[32mR$\033[m{p:.2f} aumentado em 13% é \033[32mR$\033[m{moeda.juros(p):.2f}')
