from random import randint


def sorteio():
    numeros_sorteados = []
    for numeros in range(5):
         sortear = randint(0,10)
         numeros_sorteados.append(sortear)
    return numeros_sorteados

def soma(num):
    return sum(num)

jogo = sorteio()
print(f'Os 5 valores sorteados foram: {jogo}')
print(f'Somando os valores {jogo}, temos: {soma(jogo)}')





