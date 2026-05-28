from time import sleep

from WorkspacePython.Exercicios.Exercicios_Curso_em_Video.Modulos.ex104.lib.interface import *

while True:
    resposta = menu(['Criar Arquivo','Cadastrar Pessoas','Sair do sistema'])
    if resposta == 1:
        print('Opção 01')
    elif resposta == 2:
        print("Opção 02")
    elif resposta == 3:
        print('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)