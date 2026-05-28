# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

ask= (int(input('Digite um valor: ')),
       int(input('Digite outro valor: ')),
       int(input('Digite mais um valor: ')),
       int(input('Digite o ultimo valor: ')))
print('===' *30)

print(f'O valor 9 apareceu {ask.count(9) } vezes')
if 3 in ask:
    print(f'O numero 3 apareceu na posição {ask.index(3)}')
else:
    print('O valor 3 não foi digitado nenhuma vez')
for n in ask:
    if n % 2 == 0:
        print(n,end=' ')




