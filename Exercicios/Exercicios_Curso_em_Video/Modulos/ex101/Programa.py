import moeda

numero_1 = int(input('Digite o primeiro numero: '))
numero_2 = int(input('Digite o segundo numero: '))

print(f'Soma: {moeda.aumentar(numero_1,numero_2)}')
print(f'Subtração: {moeda.diminuir(numero_1,numero_2)}')
print(f'O Dobro do numero 01: {moeda.dobro(numero_1)}\n - O Dobro do numero 02: {moeda.dobro(numero_2)}')
print(f'A metade do numero 01: {moeda.metade(numero_1)}\n - A metade do numero 02: {moeda.metade(numero_2)}')
