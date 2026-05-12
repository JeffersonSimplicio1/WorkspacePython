# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos
maior_peso = 0

print('Digite o peso de cinco pessoas: ')
for p in range(1,6):
    peso = float(input(f'Digite o peso da pessoa {p}: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'menor peso {menor}\n'
      f'maior peso {maior}')