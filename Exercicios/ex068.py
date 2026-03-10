# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time do Bahia.

times = ('Flamengo', 'Palmeiras', 'Cruzeiro','Mirassol', 'Fluminense', 'Botafogo', 'Bahia', 'São Paulo', 'Grêmio', 'Red Bull Bragantino',
         'Atlético Mineiro','Santos', 'Corinthians', 'Vasco da Gama', 'Vitória', 'Internacional', 'Ceará', 'Fortaleza', 'Juventude', 'Sport' )

print(f'Estes foram os cinco primeiros colocados: {times[:5]}')
print('==='*30)
print(f'Estes foram os quatro ultimos colocados: {times[-4:]}')
print('==='*30)
print(sorted(times))
print('==='*30)
print(f'O Bahia terminou na posição: {times.index("Bahia")+1}ª')

