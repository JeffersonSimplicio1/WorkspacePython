'''Faça um programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

Formula
F = (C * 9/5) + 32'''

temp_celsius = float(input("Qual a temperatura em celsius: "))
temp_fahrenheit = (temp_celsius * 9/5) + 32

print(f'A temperatura em fahrenheit é {temp_fahrenheit:.2f}')