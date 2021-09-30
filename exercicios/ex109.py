import moeda
p = float(input(f'Digite um preço: {moeda.preço(formatar=True)}'))
while True:
    formatar = str(input('Deseja os valores formatados?[S][N]: ')).strip().upper()[0]
    if formatar in 'SN':
        break
    else:
        print('\033[7m Resposta inválida! \033[m')
if formatar == 'S':
    f = True
else:
    f = False
print(f'a metade de {moeda.preço(p, f)} é {moeda.metade(p, f)}')
print(f'o dobro de {moeda.preço(p, f)} é {moeda.dobro(p, f)}')
print(f'o preço de {moeda.preço(p, f)} reduzido em 10% é {moeda.desconto(p, f)}')
print(f'e o preço de {moeda.preço(p, f)} aumentado em 13% é {moeda.juros(p, f)}')