# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro
# o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem
# voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
from datetime import datetime, date


def voto(ano_nascimento):
    atual_ano = date.today().year
    possibilidade = atual_ano - ano_nascimento
    if possibilidade < 16:
        print('A pessoa não pode votar\n - Status: NEGADO!')
    elif 16 <= possibilidade < 18:
        print('A pessoa pode votar opcionalmente.\n - Status: OPCIONAL!')
    else:
        print('A pessoa esta obrigada a votar\n - Status: Obrigatório!')

idade = int(input('Insira o ano do seu nascimento com quatro digitos:  '))
voto(idade)