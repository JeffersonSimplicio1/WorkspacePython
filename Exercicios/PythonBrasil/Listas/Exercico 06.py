# Faça um programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor
# a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

medias = []
cont =1
soma =0
alunoAprovados = 0

while cont <= 10:
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
print(f'Foram aprovados {alunoAprovados} aluno(s)')


