# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input('Digite o numero para saber se ele é primo: '))
total = 0
for count in range(1, numero+1):
    if(numero % count == 0):
        print('\033[34m', end = ' ')
        total += 1
    else:
        print('\033[31m', end = ' ')
    print(f'{count} ', end= ' ')
print()
print(f'\033[m O numero {numero} foi dividido {total} vezes')

if(total == 2):
    print('E por isso ele é primo!')
else:
    print('E Por isso ele não é primo')