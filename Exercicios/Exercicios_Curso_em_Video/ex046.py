# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

numero =[]
for numeros in range(1,7):
    numero_list = int(input('digite um numero: '))
    numero.append(numero_list)
print(f'Os numeros adicionados foram: {numero}')

soma = 0
for n in numero:
    if(n % 2 == 0):
        soma += n
print(f'A soma dos numeros pares é: {soma}')

