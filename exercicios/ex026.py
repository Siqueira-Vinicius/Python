print('Letra A')
frase = str(input('Redija uma frase: '))
frase = frase.strip()
frase = frase.upper()
a = frase.count('A')
p = frase.find('A') + 1
l = frase.rfind('A') + 1
print('Na sua frase a letra "A" apareceu {} vezes'
      .format(a))
print('A primeira vez que ela apareceu foi no '
      '{}º caractere'.format(p))
print('E a ultima vez que ela apareceu foi no '
      '{}º caractere'.format(l))

