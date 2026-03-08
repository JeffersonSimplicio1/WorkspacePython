print('Vamos comparar três numeros!')

numero_01 = int(input('Digite o primeiro numero: '))
print('--' * 20)
numero_02 = int(input('Digite o segundo numero: '))
print('--' * 20)
numero_03 = int(input('Digite o terceiro numero: '))
print('--' * 20)

if(numero_01 > numero_02 and numero_01 > numero_03):
    print(f'O numero {numero_01} é o MAIOR')
    if(numero_02 > numero_03):
        print(f'O numero {numero_03} é o menor')
    else:
        print(f' O numero {numero_02} é o menor')

elif(numero_02 > numero_01 and numero_02 > numero_03):
    print(f'O numero {numero_02} é o MAIOR')
    if(numero_01 > numero_03):
        print(f'O numero {numero_03} é o menor')
    else:
        print(f"O numero {numero_01} é o menor")

elif(numero_03 > numero_01 and numero_03 > numero_02):
    print(f'O numero {numero_03} é o MAIOR')
    if(numero_01 > numero_02):
        print(f'O numero {numero_02} é o menor')
    else:
        print(f'O numero {numero_01} é o menor')