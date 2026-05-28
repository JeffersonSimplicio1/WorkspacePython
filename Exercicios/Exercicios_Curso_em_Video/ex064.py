# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#
# A) quantas pessoas tem mais de 18 anos.
#
# B) quantos homens foram cadastrados.
#
# C) quantas mulheres tem menos de 20 anos.

homens = 0
maiorIdade = 0
mulherMenor = 0

while True:
    print('=-=' * 30)
    sexo = str(input('Qual o sexo da pessoa? (Homem ou Mulher)').strip().upper())
    idade = int(input('Qual a idade da pessoa? '))
    if idade >=18:
        maiorIdade +=1

    if sexo == 'MULHER' and idade < 20:
        mulherMenor +=1
    elif sexo == 'HOMEM':
        homens+=1
    quest = str(input('Você deseja cadastrar novamente? (Sim/Não)').strip().upper())
    if quest == 'NÃO':
        print('=-=' *30)
        print(f'Foram cadastrados {homens} homens\nForam cadastradas {mulherMenor} mulheres menores de 20 anos\n Ao todo foram cadastrados {maiorIdade} pessoas maiores de idade')
        print('Fim do programa')
        break
