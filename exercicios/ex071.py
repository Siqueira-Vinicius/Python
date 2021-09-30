cor = {'din': '\033[32mR$\033[m', 'excelente': '\033[1;31mexcelente\033[m'}
cedula = 50
totced = 0
titulo = '\033[1;34mBanco Vinebank\033[m'
config = len(titulo)+20
print(f'{titulo:^{config}}')
print('='*35)
saque = int(input(f'Digite o valor que deseja sacar: {cor["din"]}'))
while True:
    if saque >= cedula:
        saque -= cedula
        totced += 1
    else:
        print(f'Total de {totced} cédulas de {cor["din"]}{cedula}')
        totced = 0
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        else:
            break
print('='*35)
print(f'Volte Sempre ao Vinebank. Tenha um {cor["excelente"]} dia!')