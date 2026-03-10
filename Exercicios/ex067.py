numeros = ('zero','um','dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    entrada = int(input('Digite um valor entre 0 e 20: '))
    if entrada < 0 or entrada > 20:
        print('Tente novamente. Digite um numero entre zero e vinte: ')
    else:
        print(numeros[entrada])
        break