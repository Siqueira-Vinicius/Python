times = ('Flamengo', 'Internacional', 'Atlético-MG', 'São Paulo', 'Fluminense', 'Grêmio',
             'Palmeiras', 'Santos', 'Athletico-PR', 'Bragantino', 'Ceará SC', 'Corinthians', 'Atlético-GO',
             'Bahia', 'Sport Recife', 'Fortaleza', 'Vasco da Gama', 'Goiás', 'Coritiba', 'Botafogo')

print(f'Os \033[4;34m5\033[m primeiros colocados do \033[32mCampeonato Brasileiro de Futebol\033[m são: {times[0:5]}')
print(f'Os \033[4;31m4\033[m ultimos colocados do \033[32mCampeonato Brasileiro de Futebol\033[m são: {times[-4:]}')
print(f'Times do \033[32mCampeonato Brasileiro de Futebol\033[m em ordem alfabética: ')
for ordem in sorted(times):
    print(f'{ordem}')

print(f'O time do \033[30mCorinthians\033[m está na {times.index("Corinthians")+1}ª posição')