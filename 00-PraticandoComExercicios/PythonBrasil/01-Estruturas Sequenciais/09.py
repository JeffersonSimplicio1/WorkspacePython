'''Faça um programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

Formula
C = 5 * ((F-32) / 9).'''

temp_fahrenheit = float(input("Qual a temperatura em Fehrenheit: "))

temp_celsius = 5*((temp_fahrenheit - 32)/9)

print(f'A temperatura em Celsius é: {temp_celsius:.2f}')