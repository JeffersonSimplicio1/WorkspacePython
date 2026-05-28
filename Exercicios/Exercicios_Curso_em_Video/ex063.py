# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando
# o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
import random

cont = 0
while True:
    pc = random.randint(0, 11)
    num = int(input('Quantos dedos? '))
    quest = str(input('Par ou impar: ').strip().upper())
    print(f' você jogou {num} dedos e o pc jogou {pc}.\nO total é de {num+pc} dedos...')

    if (pc+ num) %2 == 0:
        if quest != 'PAR':
            print('A vitoria é minhaaa!!  =D')
            print(f'Você venceu {cont} vezes')
            break
        else:
            print('Você venceu!\nQuero revanche!!')
            print('=-=-'*30)
            cont +=1
    elif (pc + num) %2 !=0:
        if quest != 'IMPAR':
            print('A vitoria é minhaaa!!  =D')
            print(f'Você venceu {cont} vezes')
            break
        else:
            print('Você venceu!\nQuero revanche!!')
            cont += 1
            print('=-=-' * 30)


