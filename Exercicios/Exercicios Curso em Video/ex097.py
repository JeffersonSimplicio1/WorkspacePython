# Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e outro chamado show, que será um valor
# lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(n, show = True):
    cont = n
    numero = 0
    resposta = 1
    while cont > 0:
        if cont == n:
            numero = cont * (cont -1)
            resposta = numero
            cont -=2
        else:
            resposta *= cont
            cont -=1
    if show == True:
        print(f'{n}! = ', end='')
        for i in range(n):
            print(f'{n-i} {"=" if i == n-1 else "*"}', end='')
        print(resposta)
    else:
        print(f'A resposta é: {resposta}')


fator = int(input('Insira o numero a ser fatorado: '))
ver = str(input('Você deseja ver o processo de fatoração [S/N]? ').upper().strip())
if ver == 'S':
    ver = True
else:
    ver = False
fatorial(fator,ver)

