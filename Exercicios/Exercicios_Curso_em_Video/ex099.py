# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante
# ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico
# .Ex: n = leiaInt(‘Digite um n: ‘)

def leiaInt(msg):
   while True:
       numero = input(msg)
       if numero.isnumeric():
           print(f'Você acabou de digitar o numero {numero}')
           break
       else:
           print('Erro! Digite um numero inteiro valido')


leiaInt('Digite um numero: ')