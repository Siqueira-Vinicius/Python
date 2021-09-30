def dobro(valor, formatar):
    r = valor*2
    if formatar:
        return f'\033[32mR$\033[m{r:.2f}'
    else:
        return r


def metade(valor, formatar):
    r = valor/2
    if formatar:
        return f'\033[32mR$\033[m{r:.2f}'
    else:
        return r


def desconto(valor, descont, formatar):
    r = valor - valor*(descont/100)
    if formatar:
        return f'\033[32mR$\033[m{r:.2f}'
    else:
        return r


def juros(valor, aumento, formatar):
    r = valor + valor*(aumento/100)
    if formatar:
        return f'\033[32mR$\033[m{r:.2f}'
    else:
        return r


def preço(valor='', formatar=False):
    r = valor
    if formatar:
        if valor=='':
            return f'\033[32mR$\033[m{r}'
        else:
            return f'\033[32mR$\033[m{r:.2f}'
    else:
        return r


def resumo(valor, aumento, descont, formatar):
    p = valor
    f = formatar
    a = aumento
    d = descont
    print('\033[31m-\033[m'*50)
    print(f'\033[31m{" Resumo do Valor ":^50}\033[m')
    print('\033[31m-\033[m'*50)
    print(f'\033[31m|\033[m A metade de {preço(p, f)} é {metade(p, f)}')
    print(f'\033[31m|\033[m O dobro de {preço(p, f)} é {dobro(p, f)}')
    print(f'\033[31m|\033[m O preço de {preço(p, f)} reduzido em {d}% é {desconto(p, d, f)}')
    print(f'\033[31m|\033[m O preço de {preço(p, f)} aumentado em {a}% é {juros(p, a, f)}')
    print('\033[31m-\033[m'*50)


def formatar():
    while True:
        formatarr = str(input('Deseja os valores formatados?[S][N]: ')).strip().upper()[0]
        if formatarr in 'SN':
            break
        else:
            print('\033[7m Resposta inválida! \033[m')
    if formatarr == 'S':
        return True
    else:
        return False
