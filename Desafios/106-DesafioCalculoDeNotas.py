# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
# e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#
# Média de Aproveitamento  Conceito
# Entre 9.0 e 10.0         A
# Entre 7.5 e 9.0           B
# Entre 6.0 e 7.5           C
# Entre 4.0 e 6.0           D
# Entre 4.0 e zero         E
#
# # O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO”
# se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
from time import sleep

print('Este programa irá lhe auxiliar no calculo da media de alunos, no encaixe de conceitos e na informação de aprovação e reprovação.')
sleep(1)
decisao = str(input('Digite "Start" para iniciar o programa: ').upper().strip())
#
if decisao == 'START':
    print('Iniciando programa...')
    sleep(1)
    while True:
        nota1 = float(input('Nota 1: '))
        nota2 = float(input('Nota 2: '))

        media = (nota1+nota2)/2

        if media ==1 and media >= 9.0:
            conceito = 'A'
            situacao = 'Aprovado'
        elif media <9 and  media >= 7.5:
            conceito = 'B'
            situacao = 'Aprovado'
        elif media <7.5 and media >= 6:
            conceito = 'C'
            situacao = 'Aprovado'
        elif media < 6.0 and media >= 4.0:
            conceito = 'D'
            situacao = 'Reprovado'
        else:
            conceito = 'E'
            situacao = 'Reprovado'

        print()
        print(f'-='*30)
        print()
        print(f'As notas do aluno foram:')
        sleep(1)
        print( f'Nota 1: {nota1:.2f}')
        sleep(1)
        print(  f'Nota 2: {nota2:.2f}')
        sleep(1)
        print(  f'Media: {media:.2f}')
        sleep(1)
        print( f'O aluno se enquadra no conceito : {conceito}')
        sleep(1)
        print( f'O aluno esta {situacao}')
        sleep(1)

        continuar = str(input('Você deseja continuar adicionando alunos? (S/N): ').upper().strip())
        if continuar == 'N':
            print('   Finalizando Programa...')
            sleep(1)
            break
        elif continuar != 'S':
            print('Opção invalida!!!')
            print('   Finalizando Programa...')
            sleep(1)


else:
    print('Opção invalida!!!')
    print('   Finalizando Programa...')
    sleep(1)