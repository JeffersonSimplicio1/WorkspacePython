# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

aluno = {}

aluno['nome'] = str(input('Digite o nome do aluno: '))
aluno['media'] = float(input('Insira a media do aluno: '))

if aluno['media'] > 7:
    aluno['situação'] = 'Aprovado'
elif aluno ['media'] < 7 and aluno['media'] >= 5:
    aluno['situação'] = 'Recuperação'
elif aluno['media'] < 5:
    aluno['situação'] = 'Reprovado'
print()
print('=-='*30)
print()
for k,v in aluno.items():
    print(f'{k}: {v}')