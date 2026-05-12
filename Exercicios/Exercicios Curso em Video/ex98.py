# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros
# opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz
# de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha (nome = "< Desconhecido >", gols = 0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato')

atleta = str(input('Nome do jogador: '))
numero_gols = str(input('Número de gols: '))

if numero_gols.isnumeric():
    numero_gols = int(numero_gols)
else:
    numero_gols = 0
if atleta.strip() == '':
    ficha(gols=numero_gols)
else:
    ficha(atleta, numero_gols)