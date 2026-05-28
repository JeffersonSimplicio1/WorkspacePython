from time import sleep


def maior(* num):
    cont = 0
    maior = 0
    print('\nAnalizando os valores adicionados...')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont ==0:
            maior = valor
        else:
            if maior < valor:
                maior = valor
        cont += 1
    print(f'\nForam informados {cont} valores ao todo')
    print(f'O maior valor foi: {maior}')


#Programa principal
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()