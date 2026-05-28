# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

matriz = [[], [], []]

for i in range(0,3):
    matriz[0]. append(int(input(f'Digite o valor {i+1} da linha 1: ')))
for p in range(0,3):
    matriz[1].append(int(input(f'Digite o valor {p+1} da linha 2: ')))
for k in range(0,3):
    matriz[2].append(int(input(f'Digite o valor {k+1} da linha 3: ')))

print(f'{matriz[0]}\n{matriz[1]}\n{matriz[2]}')