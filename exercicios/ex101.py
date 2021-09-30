from datetime import datetime
def voto(ano):
    global idade
    idade = datetime.now().year - ano
    if idade < 16:
        return 'NEGADO'
    elif idade < 18:
        return 'OPCIONAL'
    else:
        return 'OBRIGATORIO'
idade = 0
tip = voto(int(input('Em que ano vc nasceu?: ')))
print(f'com {idade} anos, O seu voto é {tip}')

