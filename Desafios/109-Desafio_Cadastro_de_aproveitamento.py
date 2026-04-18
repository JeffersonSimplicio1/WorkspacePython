conjunto = []
dados_jogador = {}
gols_por_partida = []

while True:
    dados_jogador['nome'] = input('Qual o nome do jogador? ')
    partidas_jogadas = int(input(f"Quantas partidas {dados_jogador['nome']} jogou? "))

    for i in range(partidas_jogadas):
        gols = int(input(f'Quantos gols ele fez na partida {i+1}: '))
        gols_por_partida.append(gols)

    dados_jogador['total'] = sum(gols_por_partida)
    dados_jogador['gols'] = gols_por_partida.copy()

    gols_por_partida.clear()
    conjunto.append(dados_jogador.copy())
    dados_jogador.clear()

    pergunta = input('Você deseja adicionar outro jogador [S/N]? ').strip().upper()

    if pergunta == 'S':
        print('OK, vamos continuar...')
        continue

    if pergunta != 'N':
        print('ERRO! Tente novamente!')
        continue

    # ---------------- TABELA FINAL ----------------
    print()
    print('=-' * 30)
    print(f'{"cod":<5}{"nome":<15}{"gols":<20}{"total":<5}')
    print('-' * 40)

    for i, jogador in enumerate(conjunto):
        print(f"{i:<5} {jogador['nome']:<15} {str(jogador['gols']):<20} {jogador['total']:<5}")

    print('-' * 40)

    # ---------------- DETALHAMENTO ----------------
    while True:
        detalhar = input('Você deseja saber as estatísticas dos jogadores [S/N]? ').strip().upper()

        if detalhar == 'N':
            print('>>>>>>>> VOLTE SEMPRE <<<<<<<')
            break

        if detalhar != 'S':
            print('ERRO! Responda apenas S ou N!')
            continue

        while True:
            n = int(input('Escolha o jogador pelo código (999 para sair): '))

            if n == 999:
                print('Finalizando programa...')
                break

            if n < 0 or n >= len(conjunto):
                print(f'Erro!! Não existe jogador com o código {n}')
                continue

            print(f"\n--- ESTATÍSTICAS DO JOGADOR {conjunto[n]['nome'].upper()} ---")
            for i, g in enumerate(conjunto[n]['gols']):
                print(f'   => No jogo {i+1} fez {g} gols.')
            print('-' * 40)

        break

    break