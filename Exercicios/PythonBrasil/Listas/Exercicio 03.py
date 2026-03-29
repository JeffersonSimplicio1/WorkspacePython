# Faça um programa que leia 4 notas, mostre as notas e a média na tela.

notas = []
soma = 0


for i in range(0,4):
    nota = float(input(f'Digite a {i+1}° nota do aluno: '))
    soma += nota
    notas.append(nota)

media = soma/4
print()
print('===' * 30)
print()
print(f' As notas do aluno foram: {notas}')
print(f'A media anual desse aluno é: {media:.2f}')