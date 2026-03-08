# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
# foram necessários para vencer.
import random

print('Pensei em um número entre 1 e 10...')
print('Tente adivinhar!')

numero = random.randint(1, 10)
tentativas = 0

while True:
    escolha = int(input('Digite um numero entre 1 e 10: '))

    if  escolha < 1 or escolha >10:
        print("Numero fora do intervalo!\nTente novamente.")
        continue
    tentativas += 1

    if escolha == numero:
        print('Escolha correta!')
        print(f'Você precisou de {tentativas} tentativa(s) para vencer')
        break
    else:
        print('Escolha errada, Tente Novamente.')