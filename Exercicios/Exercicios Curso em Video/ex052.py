# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo =str(input('Qual o seu sexo? \nDigite "M" para Masculino ou "F" para feminino: ')).upper().strip()


while sexo != 'M' and sexo != 'F':
    print("O valor digitado esta incorreto!\n digite novamente!")
    print("="*20)
    sexo = input('Qual o seu sexo? \nDigite "M" para Masculino ou "F" para feminino: ').upper().strip()

if sexo == 'M':
    print("O sexo digitado é o masculino")
elif sexo =='F':
    print("O sexo digitado é o feminino")