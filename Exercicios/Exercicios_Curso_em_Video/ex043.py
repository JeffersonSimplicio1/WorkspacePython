# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
from time import sleep
for n in range(1,51):
    if(n%2 == 0):
        print(n)
        sleep(1)
print('fim')
