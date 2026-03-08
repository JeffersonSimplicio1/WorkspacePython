# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

soma = 0
cont = 0
while True:
    quest = int(input('Digite um numero aleatorio \n(digite 999 para parar o programa!): '))
    if(quest != 999):
        soma = soma + quest
        cont +=1
    else:
        print('~~'*20 )
        print('Você digitou o numero 999\n      Finalizando programa...')
        print('~~' * 20)
        break
print(f'Você digitou {cont} numeros antes de digitar o numero 999')
print(f'A soma de todos esses numeros é: {soma}')