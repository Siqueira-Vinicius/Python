try:
    from console_thrift import KeyboardInterruptException as KeyboardInterrupt
except ImportError:
    pass


def leiaint(msg):
    while True:
        try:
            numero = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO. Por favor, digite um numero inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mERRO. O usuário preferiu não digitar esse número!\033[m')
            return 0
        else:
            return numero


def leiafloat(msg):
    while True:
        try:
            numero = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO. Por favor, digite um numero real válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mERRO. O usuário preferiu não digitar esse número!\033[m')
            return 0
        else:
            return numero


n = leiaint('Digite um numero inteiro: ')
f = leiafloat('Digite um numero Real: ')
print(f'Voce acabou de digitar o numero inteiro {n} e o numero real {f}')
