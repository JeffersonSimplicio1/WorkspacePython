# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0,0,0],[0,0,0],[0,0,0]]
somaPar = 0
soma3 = 0
maiorL2 = 0

for l in range(0,3):
    for c in range(0,3):
        matriz [l] [c] = int(input(f'Digite o valor da linha {[l]} e coluna {[c]}'))
        if matriz [l] [c] % 2 == 0 :
            somaPar  += matriz[l][c]
        if c == 2:
            soma3 += matriz[l] [c]
        if matriz [1] [c] > maiorL2:
            maiorL2 = matriz [l] [c]
print()
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz [l] [c]}]', end=' ')
    print()
print()
print('==='*30)
print(f'A soma dos numeros pares é: {somaPar}')
print(f'A soma dos elementos da terceira coluna é: {soma3}')
print(f'O maior valor na linha 2 é: {maiorL2}')