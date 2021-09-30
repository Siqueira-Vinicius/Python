print('Começa com Santo?')
cidade = str(input('Digite o nome da cidade: '))
cidade = cidade.strip()
cidade = cidade.upper()
santo = cidade[:5]
começa = str(santo.find('SANTO'))
r = começa.replace('0', 'Sim')
r = r.replace('-1', 'Não')
print('A cidade escolhida começa com Santo?')
print('R:{}'.format(r))

