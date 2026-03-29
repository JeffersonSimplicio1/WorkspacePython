# Faça um programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

numeros = []

for i in range(0,10):
    numeros.append(float(input(f'Digite o elemento {i+1}: ')))
print()
print('===' *30)
print()
print(f'Os elementos listados foram: {numeros}')
numeros.sort(reverse=True)
print(f'Os elementos na ordem inversa são: {numeros}')
