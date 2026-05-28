# Melhore o DESAFIO 56, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
from django.template.defaultfilters import upper
from sqlparse import split

a1 = int(input('Qual o primeiro termo da PA? '))
razao = int(input('Qual a razão da PA? '))
n = 1
mais = 10
total = 0

print(f'Os {total} primeiros termos da PA são: ', end=' ')
while mais != 0:
    total = total + mais
    while n < total+1:
        an = a1 + (n-1)* razao
        print(an, end = ' -> ')
        n+=1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Você verificou {total} termos da PA')
print('FIM')
