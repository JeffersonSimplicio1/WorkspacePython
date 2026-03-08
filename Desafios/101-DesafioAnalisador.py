# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

cont_idade = 0
homem_mais_velho = 0
nome_mais_velho = ''
cont_mulher = 0

for p in range(1,5):
    nome = str(input(f'Digite o nome da pessoa {p}: '))
    sexo = input(f'{nome} é homem ou mulher? ')
    sexo = sexo.upper()
    idade = int(input(f'Qual a idade de {nome}: '))
    if(sexo == 'HOMEM'):
        if(idade > homem_mais_velho):
            homem_mais_velho = idade
            nome_mais_velho = nome
    if(sexo == 'MULHER'):
        if(idade < 20):
            cont_mulher +=1

    cont_idade += idade

media_idade = cont_idade/4
print(f' A media de idade do grupo é de: {media_idade}')
print(f'O homem mais velho do grupo é {nome_mais_velho}')
print(f'No grupo tem {cont_mulher} mulheres com menos de 20 anos')


