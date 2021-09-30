pessoas = []
lp = '\033[m'

def i(cor, simb = '|'):
    return f'{cr(cor)}{simb}{lp}'


def fund(cor):
    return f'\033[4{cor}m'


def titulo(msg, cor, linha):
    lin(linha, cor)
    print(f'{msg:^60}')
    lin(linha, cor)


def lin(linha, cor):
    print(f'{cr(cor)}{linha}{lp}'*60)


def cr(cor):
    return f'\033[3{cor}m'


def opçao(numero, msg, cor):
    print(f'{i(cor, simb = "[")}{numero}{i(cor, simb="]")} - {msg}')


def menu():
    if not arquivo('pessoas.txt'):
        criararquivo('pessoas.txt')
    while True:
        titulo(' MENU PRINCIPAL ', 4, '-')
        opçao(1, 'Ver pessoas cadastradas', 2)
        opçao(2, 'Cadastrar nova pessoa', 3)
        opçao(3, 'Sair do sistema', 1)
        lin('-', 4)
        execução(escolha())


def escolha():
    while True:
        try:
            r = int(input(f'{i(4)} Sua Opção: '))
        except (ValueError, TypeError):
            print(f'\033[7m Erro. Digite um \'número\'. {lp}')
            continue
        else:
            if r < 1 or r > 3:
                print(f'\033[7m Erro. Escolha uma opção válida(1, 2, 3)! {lp}')
                continue
            else:
                break
    lin('-', 4)
    return r


def execução(escolha):
    if escolha == 1:
        lista()
    elif escolha == 2:
        cadastro()
    elif escolha == 3:
        fim()


def lista():
    titulo('PESSOAS CADASTRADAS', 2, '-')
    leiaarquivo('pessoas.txt')
    lin('-', 2)


def cadastro():
    titulo('CADASTRO', 3, '-')
    pessoa = {}
    a = nome()
    b = idade()
    pessoa['nome'] = a
    pessoa['idade'] = b
    pessoas.append(pessoa.copy())
    msg = f'Novo registro de {a} adicionado.'
    print(f'{fund(3)} {msg:^60} {lp}')
    pessoa.clear()
    lin('-', 3)
    salvar('pessoas.txt')


def nome():
    nada = []
    ok = 0
    while True:
        nome = str(input(f'{i(3)} Nome: ')).strip().split()
        if nome == nada:
            ok = 1
        for c in nome:
            if not c.isalpha():
                ok = 1
        if ok == 1:
            print('\033[7m Informe um nome Real. \033[m')
            ok = 0
            continue
        else:
            break
    r = ' '.join(nome).title()
    return r


def idade():
    while True:
        try:
            idade = int(input(f'{i(3)} Idade: '))
        except (ValueError, TypeError):
            print('\033[7m Informe uma idade numérica (numeros inteiros). \033[m')
            continue
        else:
            return idade


def fim():
    lin('-', 1)
    print(f'{fund(1)}{"ATÉ A PRÓXIMA :)":^60}{lp}')
    lin('-', 1)
    return exit()


def arquivo(arq):
    try:
        a = open(arq, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(arq):
    try:
        a = open(arq, 'wt+')
        a.close()
    except:
        print('\033[7m Houve um erro ao criar o arquivo \033´m ')
    else:
        print(f'{fund(2)}{"Arquivo criado com sucesso!":^60}{lp}')


def leiaarquivo(arq):
    try:
        a = open(arq, 'rt')
    except:
        print('\033[7m Houve um erro ao ler o arquivo \033´m ')
    else:
        for l in a:
            dados = l.split(';')
            dados[1] = dados[1].replace('\n', '')
            print(f'{i(2)} {dados[0]:<30}{dados[1]:>20}{"anos":>5}')
    finally:
        a.close()


def salvar(arq):
    try:
        a = open(arq, 'at')
    except:
        print('\033[7m Houve um erro ao salvar o arquivo \033´m ')
    else:
        for c in pessoas:
            a.write(f'{c["nome"]};{c["idade"]}\n')
    finally:
        a.close()