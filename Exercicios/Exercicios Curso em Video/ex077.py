# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter
# apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

listaCompleta =[]
listaPares = []
listaImpares = []

while True:
    elemento = int(input('Digite um numero: '))
    listaCompleta.append(elemento)

    if elemento % 2 == 0:
        listaPares.append(elemento)
    else:
        listaImpares.append(elemento)
    pergunta = str(input('Você deseja adicionar outro elemento? (S/N) ').upper().strip())

    if pergunta == 'N':
        print('==='*30)
        print('Finalizando programa...')
        print(f'A lista de todos os elementos digitados é : {listaCompleta}')
        print(f'A lista dos numeros pares é: {listaPares}')
        print(f'A lista dos numeros impares é: {listaImpares}')
        break
    elif pergunta != 'S':
        print('==='*30)
        print('O valor digitado é invalido.\n O programa será finalizado!\n     Finalizando programa...')
        print(f'A lista de todos os elementos digitados é : {listaCompleta}')
        print(f'A lista dos numeros pares é: {listaPares}')
        print(f'A lista dos numeros impares é: {listaImpares}')
        break
