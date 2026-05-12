# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre - o(com idade)
# em um dicionário.Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de
# contratação e o salário.Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date, datetime

dados = {}

ano_atual = date.today().year
dados['nome'] = str(input('Nome: '))
anoDeNascimento = int(input('Ano de nascimento: '))
dados['idade'] = ano_atual - anoDeNascimento
dados['CTPS'] = int(input('Carteira de Trabalho (0 não tem)'))
if dados['CTPS'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salario'] = float(input('Salário: '))
    dados['Aposentadoria'] = dados['idade'] + (dados['contratação'] + 35) - ano_atual
print('=-' * 30)
for i, v in dados.items():
    print(f'       - {i} tem o valor {v} ')
