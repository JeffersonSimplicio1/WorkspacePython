#Escreva um programa que leia dois numeros inteiros e compareos, mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

numero_01 = int(input('Insira um numero: '))
numero_02 = int(input('Insira mais um numero: '))

if(numero_01>numero_02):
    print(f'O primeiro valor é maior')
elif(numero_02>numero_01):
    print('O segundo valor é maior')
else:
    print('Não existe valor maior, os dois são iguais')