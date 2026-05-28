# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome
# do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

dados_jogador = {}
partidas = []
soma_gols = 0

dados_jogador['nome'] = str(input('Nome: '))
partidasTrue = int(input('Quantidade de Partidas jogadas: '))
for i in range(partidasTrue):
    golsPartidas = int(input(f'Quantos gols na partida {i +1}: '))
    partidas.append(golsPartidas)
dados_jogador ['gols'] = partidas.copy()

# for i in partidas:
#     soma_gols += i
soma_gols = sum(partidas)
dados_jogador['total'] = soma_gols

print('=-'*30)
print(dados_jogador)

print('=-'*30)
for i, v in dados_jogador.items():
    print(f'     - O Campo {i} tem o valor {v}')

print('=-'*30)
print(f'O jogador {dados_jogador['nome']} jogou {partidasTrue} partidas.')
for i, v in enumerate(partidas):
    print(f'     => Na partida {i}, fez {v} gols')
print(f'Foi um total de {dados_jogador['total']} gols')