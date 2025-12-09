#Estrutras utilizadas para repetir um trecho de codigo.

#FOR (Utilizado quando SE SABE quantas vzs o codigo vai se repetir)

texto = input('Escreva um nome: ')
VOGAIS = "AEIOUaeiou"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra.upper(), end=" ")

print()

#FOR utilizando Range = função built-in do python, usada para produzir uma sequencia de numeros inteiros a partir de um inicio para um fim.

for num in range(11): # a função range tambem pode ser escreita range (0,11) -> (Inicio, fim)
    print(num, end = " ")
print()


for numeros in range(0,51,5): #(inicio, fim, step) STEP = pulo (O programa vai contar de 5 em 5)
    print(numeros, end=" ")