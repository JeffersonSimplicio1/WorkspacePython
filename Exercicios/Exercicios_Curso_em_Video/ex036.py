# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade , se ele ainda vai se alistar ao serviço militar,
# se é a hora de se alistar ou se já passou o tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
import datetime

ano_nascimento = int(input('Em que ano você nasceu? '))
idade = datetime.date.today().year - ano_nascimento

if(idade<18):
    print("Você ainda irá se alistar\n"
          f'Não se preocupe, falta apenas {18-idade} anos para seu alistamento!')
elif(idade >= 18 and idade <=19):
    print('Parabéns!!\n'
          'Chegou a hora do seu alistamento Militar!')
else:
    print('Que pena!!!\n'
          'Infelizmente você perdeu a epoca do alistamento militar!\n'
          f'O tempo se excedeu em  {idade - 18} anos  ')