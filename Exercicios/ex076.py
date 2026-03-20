# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista =[]
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    pergunta = str(input('Você deseja adicionar mais algum valor (S/N)? ').strip().upper())
    if pergunta == 'N':
        print('=-='*30)
        print(f'Foram adicionados {len(lista)} numeros')
        lista.sort(reverse=True)
        print(lista)

        if 5 not in lista:
            print('O numero 5 não Aparece entre os numeros digitados')
        else:
            print('O numero 5 esta entre os numeros digitados')
        break
    elif pergunta != 'S':
        print('=-=' * 30)
        print('O valor inserido não é compativel')
        print('Finalziando programa...')
        break


