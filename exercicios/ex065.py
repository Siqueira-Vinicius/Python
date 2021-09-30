simounao = ' '

maior = soma = menor = media = vezes = 0
while simounao not in 'Nn':
    n = int(input('Digite um numero: '))
    if simounao == ' ':
        menor = n
    simounao = str(input('Quer continuar?[S][N]: ')).strip()
    soma += n
    vezes += 1

    if simounao not in 'SsNn':
        print('Opção Invalida, Tente novamente')
        soma -= n
        vezes -= 1

    if n > maior and simounao in 'SsNn':
        maior = n
    if n < menor and simounao in 'SsNn':
        menor = n

media = soma / vezes
print('A media dos valores digitados é {:.2f}'.format(media))
print('O menor valor digitado foi {} e o maior foi {}'.format(menor, maior))
