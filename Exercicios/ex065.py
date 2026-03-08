# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#
# A) qual é o total gasto na compra.
#
# B) quantos produtos custam mais de R$1000.
#
# C) qual é o nome do produto mais barato.

totalGasto =0
produtosSuper1000=0
prodBarato = 0
nomeProdBarato = ''
cont = 0

while True:
    print('=-='*30)
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o valor do produto: '))

    totalGasto += preco

    if cont == 0:
        prodBarato = preco
        nomeProdBarato = nome
        cont+=1
    if preco >=1000:
        produtosSuper1000 +=1
    if preco < prodBarato:
        prodBarato = preco
        nomeProdBarato = nome
    print('=-=' * 30)
    quest = int(input('Você deseja cadastrar mais algum produto?\n1-Sim\n2-Não\n-> '))

    if quest == 2:
        print(f'Você cadastrou o total: {totalGasto} Reais')
        print(f'Você cadastrou o total de {produtosSuper1000} produtos acima de 1000 reais')
        print(f'O nome do produto mais barato é {nomeProdBarato}')
        print('Fim do programa!!')
        break