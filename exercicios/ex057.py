sexo = 0
while 2 != sexo != 1:
    sexo = int(input('Qual o seu sexo?\n[1]\033[34mMaculino\033[m\n[2]\033[31mFeminino\n\033[mR: '))
    if 2 != sexo != 1:
        print('\033[7m Opção invalida, tente novamente! \033[m')
if sexo == 1:
    print('Seu sexo é \033[4mMasculino\033[m'.format())
else:print('Seu sexo é \033[4mFeminino\033[m')