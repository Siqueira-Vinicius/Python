print('Promoção')
p = float(input('Digite o Preço do produto: R$'))
d = float(input('Digite a porcentagem do desconto: %'))
print('O produto sairá por R${:.2f} reais.'
      .format(p-(p*d/100)))
