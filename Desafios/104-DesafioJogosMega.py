# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre
# 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
import random
from random import randint
from time import sleep

lista = []
jogos = []
cont = 0

print('_' *30)
print('       Jogos da Mega Sena      ')
print('_'*30)
quant = int(input('Quantos jogos você deseja fazer? '))
print()
tot = 0
while tot< quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont +=1
        if cont >=6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot +=1
print('-=' *5, f'Sorteando {quant} jogos' , '-='*5)
print()

for i , valor in enumerate (jogos):
    print(f'Jogo {i+1}: {valor}')
    sleep(1.5)
print('-='*5, f'BOA SORTE!!', '-='*5 )