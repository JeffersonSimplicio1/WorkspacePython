# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o
# maior valor que estão na tupla.
import random

numeros = (random.randint(1,100), random.randint(1,100), random.randint(1,100),
           random.randint(1,100), random.randint(1,100))

print('Os valores sorteados foram: ', end=' ' )
for count in numeros:
    print(f'{count}', end=' ')

print(f'\nO maior valor foi: {max(numeros)}')
print(f'O menor valor foi: {min(numeros)}')

