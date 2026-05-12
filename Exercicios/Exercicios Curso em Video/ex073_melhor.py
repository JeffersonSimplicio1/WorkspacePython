lista = []
numeroMaior = 0
numeroMenor = 0

for i in range(0,5):
    lista.append(int(input(f'Digite o valor numero {i+1}: ')))
numeroMaior = max(lista)
numeroMenor = min(lista)

print('==-=='*15)
print(f'Você digitou os numeros {lista}')

print(f'O maior numero foi: {numeroMaior} e ele ocupa a(s) posição(ões):', end=' ')
for n,v in enumerate(lista):
    if v == numeroMaior:
        print(f'{n}...', end='')

print()

print(f'O menor numero foi: {numeroMenor} e ele ocupa a(s) posição(ões):', end=' ')
for n,v in enumerate(lista):
    if v == numeroMenor:
        print(f'{n}...', end='')