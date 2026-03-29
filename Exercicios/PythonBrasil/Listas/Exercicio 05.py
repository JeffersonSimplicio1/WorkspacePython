# Faça um programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
from traceback import print_tb

numeros = []
par = []
impar = []

for i in range(20):
    numero = int(input(f'Digite o {i+1}° valor: '))
    numeros.append(numero)
    if numero %2 ==0:
        par.append(numero)
    else:
        impar.append(numero)
print()
print('===' *30)
print()

print(f'Os numeros adicionados fora: {numeros}')
print(f'Foram adicionados {len(par)} pares. Os valores pares foram: {par}')
print(f'Foras adicionados  {len(impar)} impares. Os valore impares foram: {impar}')
