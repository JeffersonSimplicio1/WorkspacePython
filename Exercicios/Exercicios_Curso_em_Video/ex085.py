# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as
# notas de cada aluno individualmente.

ficha = []

while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1+nota2) /2
    ficha.append([nome, [nota1, nota2], media])

    resp = input('Deseja adicionar um novo aluno? (S/N)').upper().strip()

    if resp == 'N':
        break
    elif resp != 'S':
        print('A resposta não consta no banco de dados.\n Finalizando programa...')
        break

print('-='*30)
print(f'{'No.': <4}{'NOME':<10}{'MÉDIA':>8}')
print('_'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('===' * 30 )
    opc = int(input('Mostrar notas de qual aluno? (777 interrompe): '))
    if opc == 777:
        print('Finalizando...')
        break
    if opc <= len(ficha) -1 :
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<<<<< VOLTE SEMPRE >>>>>>>')

