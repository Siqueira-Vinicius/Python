print('Brincando com seu Nome')
nome = str(input('Digite seu nome completo: '))
maiusculo = nome.upper()
minusculo = nome.lower()
espaços = nome.count(' ')
letras = len(nome)-espaços
divisão = nome.split()
primeiro = len(divisão[0])
print('Seu nome em maiúsculo fica {}'
      .format(maiusculo))
print('Seu nome em minusculo fica {}'
      .format(minusculo))
print('A quantidade de letras do seu nome é {}'
      .format(letras))
print('E seu primeiro nome possui {} letras.'
      .format(primeiro))





