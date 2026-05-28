# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas
# já são maiores.
from datetime import date
cont_maior = 0
menor = 0

for i in range(7):
    ano = int(input('Digite o ano de nascimento: '))
    idade = date.today().year - ano
    if(idade >= 18):
        cont_maior += 1
    else:
        menor += 1
print(f'{cont_maior} Pessoas já atingitam a maior idade')
print(f'{menor} Pessoas ainda não atingiram a maior idade')