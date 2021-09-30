print(f'\033[31m{" CONTROLE DE TERRENOS ":^40}\033[m')
print('\033[31m-\033[m'*40)


def area(altura, comprimento):
    print(f'A area do terreno {altura}x{comprimento} é de {altura*comprimento}m².')


area(float(input('Digite a altura do terreno(M): ')), float(input('Digite o comprimento do terreno(M): ')))

