# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# .B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves

grupoPessoas =[]
dados =[]
maior = menor = 0

while True:
    dados.append(input('Nome: '))
    dados.append(float(input('Peso: ')))

    if len(grupoPessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]

    grupoPessoas.append(dados[:])
    dados.clear()

    cont = str(input('Deseja continuar adicionando? (S/N)').upper().strip())
    if cont == 'N':
        break
    elif cont != 'S':
        print('Resposta Invalida!')
        print('Finalizando Programa...')
        break
print('==='*30)
print(f'Os dados foram {grupoPessoas}')
print(f'Você cadastrou {len(grupoPessoas)}')
print(f'O maior peso adicionado é de  {maior} Kg')
for i in grupoPessoas:
    if i[1] == maior:
        print(f'{i[0]}', end=' ')
print(f'O menor peso adicionado é de: {menor}Kg')
for p in grupoPessoas:
    if p[1] == menor:
        print(f'{p[0]}', end=' ')