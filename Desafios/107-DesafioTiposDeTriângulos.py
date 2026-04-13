# Faça um programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores
# podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
from time import sleep

conj = []
triangulo = []

print('Este programa te ajudara a saber se os valores pode formar um triângulo e qual o tipo de triangulo do triangulo. ')
print('Iniciando Programa...')
sleep(1)
print('...')
sleep(1)

while True:
    lado1 = float(input('Lado 1: '))
    lado2 = float(input('Lado 2: '))
    lado3 = float(input('Lado 3: '))

    if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2+ lado3 > lado1:
        print('Os valores formam um triângulo.')
        triangulo.append(lado1)
        triangulo.append(lado2)
        triangulo.append(lado3)
        if lado1 == lado2 and lado2 == lado3 and lado1 == lado3:
            tipo = 'Equilátero'
            triangulo.append(tipo)
            conj.append(triangulo[:])
            triangulo.clear()
        elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
            tipo = 'Isósceles'
            triangulo.append(tipo)
            conj.append(triangulo[:])
            triangulo.clear()
        elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
            tipo= 'Escaleno'
            triangulo.append(tipo)
            conj.append(triangulo[:])
            triangulo.clear()
        novo = str(input('Você deseja testar novamente? (S/N)? ').upper().strip())
        if novo == 'N':
            print()
            print(f'Você adicionou {len(conj)} triângulos.\n')
            for i,v in enumerate(conj):
                print(f'Triângulo {i+1}')
                print(f'Lados: {v[0]}, {v[1]},{v[2]}')
                print(f'Tipo: {v[3]}')
                print('-='*30)
            break
        elif novo != 'S':
            print()
            print('Valor Invalido...')
            print(f'Você adicionou {len(conj)} triângulos.\n')
            for i,v in enumerate(conj):
                print(f'Triângulo {i + 1}')
                print(f'Lados: {v[0]}, {v[1]},{v[2]}')
                print(f'Tipo: {v[3]}')
                print('-=' * 30)
            print('Finalizando Programa...')
            sleep(1)
            break

    else:
        print('Os valores não formam um triângulo.')
        print('Finalizando programa...')

        novo = str(input('Você deseja adicionar novos valores (S/N)? ').upper().strip())
        if novo == 'N':
            print('Finalizando programa...')
            sleep(1)
            break
        if novo != 'S':
            print('Valor invalido...')
            print('...')
            sleep(1)
            print('Finalizando Programa...')
            break
