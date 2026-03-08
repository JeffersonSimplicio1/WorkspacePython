import random
from random import randint

print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
numero = randint(0,5)
ask = int(input('Em que numero eu pensei? '))

if(ask ==numero):
    print('PROCESSANDO...')
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('PROCESSANDO...')
    print(f'GANHEI! Eu pensei no numero {numero} e não no {ask}')
