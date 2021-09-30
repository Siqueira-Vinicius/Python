from datetime import datetime
aposentadoria = {}
aposentadoria['Nome'] = str(input('Informe seu nome: '))
idade = int(input('Em que ano você nasceu?: '))
aposentadoria['Idade'] = (datetime.now().year - idade)
aposentadoria['CTPS'] = int(input('Numero da carteira de trabalho(0 se não tiver): '))
if aposentadoria['CTPS'] != 0:
    aposentadoria['Ano de contratação'] = int(input('Ano de contratação: '))
    aposentadoria['Salario'] = float(input('salario: R$'))
    aposentadoria['aposentadoria'] = (aposentadoria['Ano de contratação'] - idade) + 35
for k, v in aposentadoria.items():
    print(f'{k}: {v}')
