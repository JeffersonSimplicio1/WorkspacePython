#Escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual sera a base de conversão:
# 1- Para binario
#  2- para Octal
# 3- para hexadeimal

numero = int(input('Digite um numero inteiro: '))
base = int(input('Qual sera a base de conversão: \n'
                 'digite: \n'
                 '1- para binário\n'
                 '2- para Octal\n'
                 '3- Para Hexadecimal\n'
                 '->  '))
if(base == 1):
    print(f'O numero {numero} convertido para binario é: {bin(numero)[2:]}')
elif(base == 2):
    print(f'O numero {numero} convertido para Octal é: {oct(numero)[2:]}')
elif(base ==3):
    print(f'O numero {numero} convertido para Hexadecimal é: {hex(numero)[2:]}')
else:
    print('A opção desejada é invalida!\n'
          'Tente novamente')