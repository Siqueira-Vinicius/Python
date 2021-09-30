cores = {'limpa': '\033[m',
         'titulo': '\033[1;34m'}


soma = 0
media = 0
velho = 0
hvelho = ''
novinhas = 0
numhomem = 0
nummulher = 0

for c in range(1, 5):
    print('{}{} {}{} {}{}'.format(cores['titulo'],'-'*10, c, 'ª Pessoa','-'*10, cores['limpa']))
    nome = str(input('Nome: '.format(c))).strip().capitalize()
    idade = int(input('Idade: '.format(nome)))
    sexo = int(input('{:^15} \n[1]Masculino \n[2]Feminino\nR: '.format('Sexo')))
    soma += idade

    if sexo == 1:
        numhomem += 1
        if idade > velho:
            velho = idade
            hvelho = nome

    elif sexo == 2:
        nummulher += 1
        if idade < 20:
            novinhas += 1

    elif sexo != 1 and sexo != 2:
        print('opção invalida, tente denovo!')
        exit()

media = soma / 4
print('A média de idade do grupo é {:.0f}'.format(media))

if numhomem == 0:
    print('Não há homens')

else:
    print('O homem mais velho tem {} anos e se chama {}'.format(velho, hvelho))

if novinhas == 0:
    print('Nenhuma mulher tem menos de 20 anos'.format(novinhas))
    
else:
    print('{} mulheres tem menos de 20 anos'.format(novinhas))


