# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre - os em uma
#,lista única que mantenha separados os valores pares ímpares.No final, mostre os valores e ímpares em ordem crescente.

listaPrinc = [[] , []]
valor = 0

for i in range(0,7):
    valor = int(input(f'Digite o valor {i+1}: '))
    if valor % 2 == 0:
        listaPrinc[0].append(valor)
    else:
        listaPrinc[1].append(valor)

print()
print('==='*30)
print()
listaPrinc[0].sort()
listaPrinc[1].sort()
print(f'Os valores pares digitados na lista foram: {listaPrinc[0]}')
print(f'Os valores impares digitados na lista foram: {listaPrinc[1]}')
