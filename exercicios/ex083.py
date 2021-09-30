parenteses = []

expressão = str(input('Digite a expressão: '))

for elemento in expressão:
    if elemento in '(':
        parenteses.append('(')
    elif elemento in ')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(')')
            break
if len(parenteses) == 0:
    print('Expressão \033[32mcorreta\033[m!')
else:
    print('Expressão \033[31mIncorreta\033[m!')
