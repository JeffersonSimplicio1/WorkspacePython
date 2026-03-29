# Faça um programa que pergunte a quantidade de alunos que serão cadastradas as notas e peça as quatro notas deles,
# calcule e armazene num vetor a média de cada aluno, imprima as medias dos alunos e o número de alunos com média maior ou igual a 7.0.

medias = []
cont =1
quantidade = int(input('As notas de quantos alunos serçao cadastradas? '))
soma =0
alunoAprovados = 0

while cont <= quantidade:
    for i in range(4):
        notas = float(input(f'Digite a {i+1}° nota do aluno {cont}: '))
        soma +=notas
    print('==='*30)
    media = round(soma/4,2)
    medias.append(media)
    soma = 0
    cont += 1

for i, valor in enumerate(medias):
    if valor >= 7:
        alunoAprovados += 1
print(f'As medias dos alunos foram: {medias}')
print(f'Foram aprovados {alunoAprovados} aluno(s)')



