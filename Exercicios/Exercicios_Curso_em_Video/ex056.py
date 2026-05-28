# Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while

a1 = int(input('Qual o primeiro termo da PA? '))
razao = int(input('Qual a razão da PA? '))
n = 1

print(f'Os 10 primeiros termos da PA são: ', end=' ')
while n < 11:

    an = a1 + (n-1)* razao
    print(an, end = ' ')
    print( ', ' if n < 10 else '.', end='')
    n+=1
# for n in range (a1,a10+1,razao):
#     print(n)