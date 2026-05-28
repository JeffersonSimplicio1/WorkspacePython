# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
# foram necessários para vencer.
import random

print('Pensei em um numero...\nDescubra em que numero eu pensei')
numero = random.randint(1,10)

escolha = int(input('De 1 até 10 em que numero eu pensei? '))
cont_erro = 0

while escolha >= 1 and escolha <= 10:
    if escolha != numero:
        print("Escolha errada")
        while escolha != numero:
            cont_erro += 1
            escolha = int(input('De 1 até 10 em que numero eu pensei? '))

    else:
        print("Escolha correta")
        print(f'Você errou {cont_erro} vezes até acertar')
        break
else:
    print("O valor digitado esta fora do intervalo de numeros que pensei")

