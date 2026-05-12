# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

a1 = int(input('Qual o primeiro termo da PA? '))
razao = int(input('Qual a razão da PA? '))
a10 = a1 + (10-1)* razao

for n in range (a1,a10+1,razao):
    print(n)