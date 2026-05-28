# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e
# todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

dados = {}
grupo = []
mulheres = []
idades = []

while True:
    dados['nome'] = str(input('Nome: '))
    dados['idade'] = int(input('Idade: '))
    idades.append(dados['idade'])
    while True:
        dados['genero'] = str(input('Sexo: [M/F] ').upper().strip())
        if dados['genero'] != 'M' and dados['genero'] != 'F':
            print('ERRO! Por favor, digite apenas M ou F.')
        else:
            if dados['genero'] == 'F':
                    mulheres.append(dados['nome'])
            grupo.append(dados.copy())
            break
    media = sum(idades) / len(idades)
    while True:
        pergunta = str(input('Quer continuar? [S/N]').upper().strip())
        if pergunta == 'N':
            print()
            print('=-' * 30)
            print()
            print(f'Ao todo temos {len(grupo)} pessoas cadastradas')
            print(f'A media de idade é de {media:.2f} anos.')
            print(f'As mulheres cadastradas foram: {mulheres}')
            print('Lista das pessoas acima da média: ')
            for dados in grupo:
                if dados['idade'] >= media:
                    print('         ', end='')
                    for i, v in dados.items():
                        print(f'{i} = {v}; ', end='')
                    print()
            print('<<<<<<< ENCERRADO >>>>>>>')
            break
        elif pergunta != 'S':
            print('ERRO! Responda a pergunta com S ou N')
        elif pergunta == 'S':
            print('Vamos continuar...')
            break