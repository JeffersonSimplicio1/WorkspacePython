# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.


valor1 = float(input('Digite um valor: '))
valor2 = float(input('Digite o segundo valor: '))



while True:
    menu = int(input( 'Digite a opção que você deseja: \n 1 - Somar\n 2 - Multiplicar\n 3 - Maior\n 4 - Novos numeros\n 5 - Sair do programa '))
    if menu == 1:
        result = valor1 + valor2
        print(f'A soma de {valor1} + {valor2} = {result}')
    elif menu == 2:
        result = valor1 * valor2
        print(f'O produto de  {valor1} * {valor2} = {result}')
    elif menu == 3:
        if valor1 > valor2:
            print(f'O maior valor é {valor1}')
        else:
            print(f'O maior valor é {valor2}')
    elif menu == 4 :
        while menu == 4:
            valor1 = float(input('Digite um valor: '))
            valor2 = float(input('Digite o segundo valor: '))
            menu = int(input('Digite a opção que você deseja: \n 1 - Somar\n 2 - Multiplicar\n 3 - Maior\n 4 - Novos numeros\n 5 - Sair do programa '))
    elif menu == 5:
        print('Finalizando programa!')
        break