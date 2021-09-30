def fatorial(numero, show=False):
    """ Função Fatorial()
        fatoria(numero, show = false)
        numero : numero inteiro
        show = True: mostrar contagem
               False : não mostrar contagem
               None : considera False
        ex:
        fatorial(5, True)
        5x4x3x2x1 = 120
    """
    f = 1
    lista = []
    for c in range(numero, 0, -1):
        f *= c
        print(f)
        lista.append(c)
        lista.append('x')
        if c == 1:
            lista.pop()
    if show == True:
        lista.append(' = ')
        lista.append(f)
        return lista
    else:
        return f


print(fatorial(3, True))


