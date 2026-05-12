# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre
# 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
import random

cartela =[]
jogo =[]

pergunta = int(input('Quantos jogos você deseja gerar? '))
cont = 0

while cont < pergunta:
    for n in range(0,6):
        sorteio = random.randint(1,60)
        if sorteio not in jogo:
            jogo.append(sorteio)
        else:
            sorteio = random.randint(1, 60)
            jogo.append(sorteio)
    cartela.append(jogo[:])
    jogo.clear()
    cont += 1
print(cartela)