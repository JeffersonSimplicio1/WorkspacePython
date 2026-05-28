# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e
# qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
soma = 0
cont = 0

while True:
    numero = int(input('Digite um numero: '))
    if cont == 0:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

    soma += numero
    cont += 1

    pergunta = input('Quer continuar? [S/N]').upper().strip()
    if pergunta == 'N':
        break

media = soma / cont
print(f'Você digitou {cont} numeros e a media deles foi {media:.2f}')
print(f'O maior valor foi {maior} e o menor valor foi {menor}')