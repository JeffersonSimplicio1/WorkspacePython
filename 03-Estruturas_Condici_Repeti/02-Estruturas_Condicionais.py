# --- Estruturas Condicionais ---

#Permitem o desvio de fluxo de controle, quando determinadas expressões logicas são atendidas.
# - IF: o comando ira testar a expressão logica e em caso de retorno verdadeiro as ações serão executadas

saldo = 2000.0
saque = float(input('Qual o valor do saque: '))

if saldo >= saque:
    print('Realizando saque!')


#if/else: Estrutura de codigo com dois desvios; Se a logica for verdadeira sera executado o bloco IF caso contrario, sera executado o bloco else.

saldo = 2000.0
saque = float(input('Qual o valor do saque: '))

if(saldo >= saque):
   print('Realizando saque')
else:
    print('Saldo insulficiente.')

# Elif: Estrutura com mais de dois desvios.

saldo = 500.0
opcao = int(input('Informe a opcao: \n'
' 1- Sacar \n' \
' 2- Extrato \n' \
' 3- Deposito\n'))

if(opcao == 1):
    valor = float(input('Qual o valor do saque: '))
    if(valor < saldo):
        print('Iniciando Saque!')
    else: 
        print('Impossivel sacar o valor informado!')
elif (opcao == 2):
    print('Imprimindo extrato!!')
    print('O saldo da sua conta é: ', saldo)
elif(opcao == 3):
    valor = float(input('Informe o valor a ser depositado: '))
    if(valor > 0):
        print('Depositando valor!')
        print('Valor depositado!\n' \
        '     Obrigado por ser nosso cliente!')
    else:
        print('O valor informado é invalido')
else:
    print('Opção invalida!')