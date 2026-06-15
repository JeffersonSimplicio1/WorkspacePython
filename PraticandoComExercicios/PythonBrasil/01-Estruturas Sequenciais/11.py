'''Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:

1- O produto do dobro do primeiro com metade do segundo .
2- A soma do triplo do primeiro com o terceiro.
3- O terceiro elevado ao cubo.'''

numero1 = int(input("Digite um numero inteiro: "))
numero2 = int(input("Digite mais um numero inteiro: "))
numero3 = float(input("Digite um numero real: "))

resp1 = (numero1*2) * (numero2/2)
resp2 = (numero1*3) + numero3
resp3 = numero3**3

print(f'O produto do dobro do primeiro com metade do segundo: {resp1} \nA soma do triplo do primeiro com o terceiro: {resp2:.2f} \nO terceiro elevado ao cubo: {resp3:.2f}')