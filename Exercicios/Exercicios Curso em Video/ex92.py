# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
# Ex:
# escreva(‘Olá, Mundo!’) Saída:
# ~~~~~~~~~
# Olá, Mundo!
# ~~~~~~~~~

def escreva (msgm):
    tam = len(msgm) + 4
    print('~'*tam)
    print(f'    {msgm}')
    print('~'*tam)

# Programa principal
inserir = str(input('Digite algo: '))
escreva(inserir)