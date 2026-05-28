# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120

numero = int(input('Digite o numero que você quer fatorar: '))
cont = numero
fator = 1
print(f'Calculando {numero}! = ', end=' ')
while cont > 0:
    print(f'{cont} ', end=' ')
    print(' x ' if cont > 1  else ' =', end=' ')
    fator *= cont
    cont -= 1
print(fator)
