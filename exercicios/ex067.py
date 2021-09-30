while True:
    numero = int(input('Digite um numero: '))
    if numero < 0:
        print('Numero negativos são invalidos. Fim do programa')
        break
    for c in range(1,11):
        print(f'{numero} x {c:2} = {numero*c}')


