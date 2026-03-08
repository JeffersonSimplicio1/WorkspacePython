import random
from random import randint

humano = int(input('Escolha uma opção: \n'
                   '0 - Pedra\n'
                   '1 - Papel\n'
                   '2 - Tesoura '))
escolha_humano = ''

if(humano == 0):
    escolha_humano = 'Pedra'
elif(humano == 1):
    escolha_humano = 'Papel'
elif(humano == 2):
    escolha_humano = 'Tesoura'

pc = randint(0,2)
escolha_pc = ''

if(pc == 0):
    escolha_pc = 'Pedra'
elif(pc == 1):
    escolha_pc = 'Papel'
elif(pc == 2):
    escolha_pc = 'Tesoura'

if(humano == pc):
    print(f'O computador escolheu {escolha_pc} e você escolheu {escolha_humano}\n'
          f'Vocês escolheram a mesma opção\n'
          f'Não houve vencedor')
elif(humano == 0 and pc == 2):
    print(f'O computador escolheu {escolha_pc} e você escolheu {escolha_humano}\n'
          f'Você venceu!!')
elif(humano == 2 and pc ==0):
    print(f'O computador escolheu {escolha_pc} e você escolheu {escolha_humano}\n'
          f'Você Perdeu!!')
elif(humano == 1 and pc ==0):
    print(f'O computador escolheu {escolha_pc} e você escolheu {escolha_humano}\n'
          f'Você Venceu!')
elif(humano == 0 and pc == 1):
    print(f'O computador escolheu {escolha_pc} e você escolheu {escolha_humano}\n'
          f'Você Perdeu')
elif(humano == 2 and pc == 1):
    print(f'O computador escolheu {escolha_pc} e você escolheu {escolha_humano}\n'
          f'Você Venceu!')
elif(humano == 1 and pc == 2):
    print(f'O computador escolheu {escolha_pc} e você escolheu {escolha_humano}\n'
          f'Você Perdeu!!')
