# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juro

opcao = int(input('Escolha uma forma de pagamento:\n'
                  '1 - À vista dinheiro/ Cheque\n'
                  '2 - À vista no cartão\n'
                  '3 - Em até 2x no cartão\n'
                  '4 - 3x ou mais no cartão\n'
                  '   ->'))
print()
if(opcao == 1):
    print('Você recebeu 10 % de desconto')
elif(opcao == 2 ):
    print('Você recebeu 5% de desconto')
elif(opcao == 3):
    print('Essa modalidade não dispõe de desconto')
elif(opcao == 4 ):
    print('O valor receberá um acrescimo de 20% referente aos juros')