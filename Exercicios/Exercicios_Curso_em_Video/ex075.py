# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção
# (sem usar o sort()). No final, mostre a lista ordenada na tela.

numeros = []

for c in range(0,5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > numeros[-1]:
        numeros.append(n)
    else:
        pos = 0
        while pos < len(numeros):
            if n <= numeros[pos]:
                numeros.insert(pos, n)
                break
            pos += 1
print(f'Os valores  adicionados foram: {numeros}')